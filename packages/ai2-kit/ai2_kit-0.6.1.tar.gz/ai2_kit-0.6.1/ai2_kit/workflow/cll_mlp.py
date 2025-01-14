from ai2_kit.core.executor import BaseExecutorConfig
from ai2_kit.core.artifact import ArtifactMap
from ai2_kit.core.log import get_logger
from ai2_kit.core.util import load_yaml_files, merge_dict
from ai2_kit.core.resource_manager import ResourceManager
from ai2_kit.core.checkpoint import set_checkpoint_file, apply_checkpoint
from ai2_kit.domain import (
    deepmd,
    iface,
    lammps,
    lasp,
    selector,
    cp2k,
    vasp,
    constant as const,
    updater,
)

from pydantic import BaseModel
from typing import Dict, List, Optional, Any
from fire import Fire

import asyncio
import itertools
import copy
import os

logger = get_logger(__name__)


class CllWorkflowExecutorConfig(BaseExecutorConfig):
    class Context(BaseModel):
        class Train(BaseModel):
            deepmd: deepmd.CllDeepmdContextConfig

        class Explore(BaseModel):
            lammps: Optional[lammps.CllLammpsContextConfig]
            lasp: Optional[lasp.CllLaspContextConfig]

        class Label(BaseModel):
            cp2k: Optional[cp2k.CllCp2kContextConfig]
            vasp: Optional[vasp.CllVaspContextConfig]

        train: Train
        explore: Explore
        label: Label

    context: Context


class WorkflowConfig(BaseModel):
    class General(BaseModel):
        type_map: List[str]
        mass_map: List[float]
        max_iters: int = 1

    class Label(BaseModel):
        cp2k: Optional[cp2k.CllCp2kInputConfig]
        vasp: Optional[vasp.CllVaspInputConfig]

    class Train(BaseModel):
        deepmd: deepmd.CllDeepmdInputConfig

    class Explore(BaseModel):
        lammps: Optional[lammps.CllLammpsInputConfig]
        lasp: Optional[lasp.CllLaspInputConfig]

    class Select(BaseModel):
        model_devi: selector.CllModelDeviSelectorInputConfig

    class Update(BaseModel):
        walkthrough: updater.CllWalkthroughUpdaterInputConfig

    general: General
    train: Train
    explore: Explore
    select: Select
    label: Label
    update: Update


class CllWorkflowConfig(BaseModel):

    executors: Dict[str, CllWorkflowExecutorConfig]
    artifacts: ArtifactMap
    workflow: Any  # Keep it raw here, it should be parsed later in iteration


def run_workflow(*config_files, executor: Optional[str] = None,
                 path_prefix: Optional[str] = None, checkpoint: Optional[str] = None):
    """
    Run Closed-Loop Learning (CLL) workflow to train Machine Learning Potential (MLP) models.
    """
    if checkpoint is not None:
        set_checkpoint_file(checkpoint)

    config_data = load_yaml_files(*config_files)
    config = CllWorkflowConfig.parse_obj(config_data)

    if executor not in config.executors:
        raise ValueError(f'executor {executor} is not found')
    if path_prefix is None:
        raise ValueError('path_prefix should not be empty')

    iface.init_artifacts(config.artifacts)
    resource_manager = ResourceManager(
        executor_configs=config.executors,
        artifacts=config.artifacts,
        default_executor=executor,
    )
    return asyncio.run(cll_mlp_training_workflow(config, resource_manager, executor, path_prefix))


async def cll_mlp_training_workflow(config: CllWorkflowConfig, resource_manager: ResourceManager, executor: str, path_prefix: str):
    context_config = config.executors[executor].context
    raw_workflow_config = copy.deepcopy(config.workflow)

    # output of each step
    label_output: Optional[iface.ICllLabelOutput] = None
    selector_output: Optional[iface.ICllSelectorOutput] = None
    train_output: Optional[iface.ICllTrainOutput] = None
    explore_output: Optional[iface.ICllExploreOutput] = None

    # cursor of update table
    update_cursor = 0

    # Start iteration
    for i in itertools.count(0):

        # parse workflow config
        workflow_config = WorkflowConfig.parse_obj(raw_workflow_config)
        if i >= workflow_config.general.max_iters:
            logger.info(f'Iteration {i} exceeds max_iters, stop iteration.')
            break

        # shortcut for type_map and mass_map
        type_map = workflow_config.general.type_map
        mass_map = workflow_config.general.mass_map

        # decide path prefix for each iteration
        iter_path_prefix = os.path.join(path_prefix, f'iters-{i:03d}')
        # prefix of checkpoint
        cp_prefix = f'iters-{i:03d}'

        # label
        if workflow_config.label.cp2k and context_config.label.cp2k:
            cp2k_input = cp2k.CllCp2kInput(
                config=workflow_config.label.cp2k,
                type_map=type_map,
                system_files=[] if selector_output is None else selector_output.get_model_devi_dataset(),
                initiated=i > 0,
            )
            cp2k_context = cp2k.CllCp2kContext(
                config=context_config.label.cp2k,
                path_prefix=os.path.join(iter_path_prefix, 'label-cp2k'),
                resource_manager=resource_manager,
            )
            label_output = await apply_checkpoint(f'{cp_prefix}/label-cp2k')(cp2k.cll_cp2k)(cp2k_input, cp2k_context)

        elif workflow_config.label.vasp and context_config.label.vasp:
            vasp_input = vasp.CllVaspInput(
                config=workflow_config.label.vasp,
                type_map=type_map,
                system_files=[] if selector_output is None else selector_output.get_model_devi_dataset(),
                initiated=i > 0,
            )
            vasp_context = vasp.CllVaspContext(
                config=context_config.label.vasp,
                path_prefix=os.path.join(iter_path_prefix, 'label-vasp'),
                resource_manager=resource_manager,
            )
            label_output = await apply_checkpoint(f'{cp_prefix}/label-vasp')(vasp.cll_vasp)(vasp_input, vasp_context)

        else:
            raise ValueError('No label method is specified')

        # return if no new data is generated
        if i > 0 and len(label_output.get_labeled_system_dataset()) == 0:
            logger.info("No new data is generated, stop iteration.")
            break

        # train
        if workflow_config.train.deepmd:
            deepmd_input = deepmd.CllDeepmdInput(
                config=workflow_config.train.deepmd,
                type_map=type_map,
                old_dataset=[] if train_output is None else train_output.get_training_dataset(),
                new_dataset=label_output.get_labeled_system_dataset(),
                initiated=i > 0,
            )
            deepmd_context = deepmd.CllDeepmdContext(
                path_prefix=os.path.join(iter_path_prefix, 'train-deepmd'),
                config=context_config.train.deepmd,
                resource_manager=resource_manager,
            )
            train_output = await apply_checkpoint(f'{cp_prefix}/train-deepmd')(deepmd.cll_deepmd)(deepmd_input, deepmd_context)

        else:
            raise ValueError('No train method is specified')

        # explore
        if workflow_config.explore.lammps and context_config.explore.lammps:
            lammps_input = lammps.CllLammpsInput(
                config=workflow_config.explore.lammps,
                type_map=type_map,
                mass_map=mass_map,
                dp_models={'': train_output.get_mlp_models()},
                preset_template='default',
            )
            lammps_context = lammps.CllLammpsContext(
                path_prefix=os.path.join(iter_path_prefix, 'explore-lammps'),
                config=context_config.explore.lammps,
                resource_manager=resource_manager,
            )
            explore_output = await apply_checkpoint(f'{cp_prefix}/explore-lammps')(lammps.cll_lammps)(lammps_input, lammps_context)

        elif workflow_config.explore.lasp and context_config.explore.lasp:
            lasp_input = lasp.CllLaspInput(
                config=workflow_config.explore.lasp,
                type_map=type_map,
                mass_map=mass_map,
                models=train_output.get_mlp_models(),
            )
            lasp_context = lasp.CllLaspContext(
                config=context_config.explore.lasp,
                path_prefix=os.path.join(iter_path_prefix, 'explore-lasp'),
                resource_manager=resource_manager,
            )
            explore_output = await apply_checkpoint(f'{cp_prefix}/explore-lasp')(lasp.cll_lasp)(lasp_input, lasp_context)

        else:
            raise ValueError('No explore method is specified')

        # select
        if workflow_config.select.model_devi:
            selector_input = selector.CllModelDeviSelectorInput(
                config=workflow_config.select.model_devi,
                model_devi_data=explore_output.get_model_devi_dataset(),
                model_devi_file=const.MODEL_DEVI_OUT,
                type_map=type_map,
            )
            selector_context = selector.CllModelDevSelectorContext(
                path_prefix=os.path.join(iter_path_prefix, 'selector-model-devi'),
                resource_manager=resource_manager,
            )
            selector_output = await apply_checkpoint(f'{cp_prefix}/selector-model-devi')(selector.cll_model_devi_selector)(selector_input, selector_context)

        else:
            raise ValueError('No select method is specified')

        # Update
        update_config = workflow_config.update.walkthrough

        # nothing to update because the table is empty
        if not update_config.table:
            continue
        # keep using the latest config when it reach the end of table
        if update_cursor >= len(update_config.table):
            continue

        # move cursor to next row if passing rate pass threshold
        if selector_output.get_passing_rate() > update_config.passing_rate_threshold:
            raw_workflow_config = merge_dict(copy.deepcopy(
                config.workflow), update_config.table[update_cursor])
            update_cursor += 1


if __name__ == '__main__':
    # use python-fire to parse command line arguments
    Fire(run_workflow)
