DP_CHECKPOINT_FILE = 'model.ckpt'
DP_DISP_FILE = 'lcurve.out'
DP_PROFILING_FILE = 'timeline.json'
DP_INPUT_FILE = 'input.json'
DP_FROZEN_MODEL = 'frozen_model.pb'
DP_ORIGINAL_MODEL = 'original_model.pb'

MODEL_DEVI_OUT = 'model_devi.out'
MODEL_DEVI_NEU_OUT = 'model_devi_neu.out'
MODEL_DEVI_RED_OUT = 'model_devi_red.out'

LAMMPS_DUMP_DIR = 'traj'
LAMMPS_DUMP_SUFFIX = '.lammpstrj'

SELECTOR_OUTPUT = 'selector_output'


DEFAULT_LASP_IN = {
    "Run_type": 15,
    "SSW.SSWsteps": 20,
    "SSW.Temp": 300,
    "SSW.NG": 10,
    "SSW.NG_cell": 8,
    "SSW.ds_atom": 0.6,
    "SSW.ds_cell": 0.5,
    "SSW.ftol": 0.05,
    "SSW.strtol": 0.05,
    "SSW.MaxOptstep": 300,
    "SSW.printevery": "T",
    "SSW.printselect": 0,
    "SSW.printdelay": -1,
    "SSW.output": "F"
}


DEFAULT_LAMMPS_TEMPLATE_FOR_DP_SSW = """\
units           metal
boundary        p p p
atom_style      atomic
atom_modify map yes

$$read_data_section

$$force_field_section

compute peratom all pressure NULL virial
"""


DEFAULT_ASAP_ASCF_DESC = {
    'preset': None,
    # those params following the convention of dscribe
    # https://singroup.github.io/dscribe/latest/tutorials/descriptors/acsf.html
    'r_cut': 3.5,

    'reducer_type': 'average',
    'element_wise': False,
    'zeta': 1,
}


DEFAULT_ASAP_SOAP_DESC = {
    'preset': None,

    # those params following the convention of dscribe
    # https://singroup.github.io/dscribe/latest/tutorials/descriptors/soap.html
    'r_cut': 3.5,
    'n_max': 6,
    'l_max': 6,
    'sigma': 0.5,

    'crossover': False,
    'rbf': 'gto',

    'reducer_type': 'average',
    'element_wise': False,
    'zeta': 1,
}

DEFAULT_ASAP_PCA_REDUCER = {
    'type': 'PCA',
    'parameter': {
        'n_components': 3,
        'scalecenter': True,
    }
}

# LAMMPS

_DEFAULT_LAMMPS_TOP = '''\
$$VARIABLES
$$EXTRA_VARS

$$INITIALIZE

$$POST_INIT

$$READ_DATA
$$POST_READ_DATA

$$MASS_MAP

$$SET_ATOM_TYPE
'''

_DEFAULT_LAMMPS_BOTTOM = '''\
$$POST_FORCE_FIELD

$$SIMULATION
$$POST_SIMULATION

$$RUN
$$POST_RUN
'''

_DP_FORCE_FIELD = '''\
pair_style deepmd $$DP_MODELS out_freq ${THERMO_FREQ} out_file model_devi.out
pair_coeff * *
'''

_DP_FEP_DUAL_FORCE_FIELD = '''\
variable LAMBDA_i equal 1-v_LAMBDA_f

pair_style  hybrid/overlay &
            deepmd $$DP_NEU_MODELS out_freq ${THERMO_FREQ} out_file model_devi_neu.out &
            deepmd $$DP_RED_MODELS out_freq ${THERMO_FREQ} out_file model_devi_red.out
pair_coeff  * * deepmd 1 *
pair_coeff  * * deepmd 2 *

fix PES_Sampling all adapt 0 &
    pair deepmd:1 scale * * v_LAMBDA_f &
    pair deepmd:2 scale * * v_LAMBDA_i
'''

_DP_FEP_UNI_FORCE_FIELD = '''\
variable LAMBDA_i equal 1-v_LAMBDA_f

pair_style  hybrid/overlay &
            $$PAIR_STYLE_EXT &
            deepmd $$DP_MODELS_0 type_order $$DP_FEP_INI_TYPE_ORDER &
            deepmd $$DP_MODELS_0 type_order $$DP_FEP_FIN_TYPE_ORDER
$$PAIR_COEFF_EXT
pair_coeff  * * deepmd 1 *
pair_coeff  * * deepmd 2 *

fix PES_Sampling all adapt 0 &
    pair deepmd:1 scale * * v_LAMBDA_f &
    pair deepmd:2 scale * * v_LAMBDA_i
'''

def _get_fep_rerun_setting(ns: str, in_data:str, in_traj: str):
    return f'''\
clear
# Rerun model deviation: {ns}
shell mkdir traj-{ns}
$$INITIALIZE
read_data {in_data}
$$MASS_MAP_BASE
$$POST_READ_DATA

pair_style deepmd $$DP_MODELS out_freq 1 out_file model_devi_{ns}.out type_order $$DP_DEFAULT_TYPE_ORDER
pair_coeff * *

thermo 1
thermo_style custom step temp pe ke etotal
thermo_modify format float %15.7f
dump 1 all custom 1 traj-{ns}/*.lammpstrj id type x y z
rerun {in_traj} first 0 last 1000000000000 every 1 dump x y z box yes
'''

# Notes
# 1. LAMMPS shell command use triple quote to pass a string with space and special chars in it.
# e.g """ "$$SPECORDER" """
# 2. ase read lammps-data format need to set style to "atomic"
# ref: https://gitlab.com/ase/ase/-/issues/1126
_FEP_UNI_BOTTOM = '\n'.join(['''\
# Run post processing script
shell env > debug.env.txt
shell cat traj/*.lammpstrj > traj.lammpstrj
shell cp ${DATA_FILE} ini.data
clear
shell $$AI2KIT_CMD tool ase read traj.lammpstrj --format lammps-dump-text --specorder """ "$$SPECORDER" """ - write ini.lammpstrj --format lammps-dump-text  --type_map """ "$$SPECORDER_BASE" """
shell $$AI2KIT_CMD tool ase read traj.lammpstrj --format lammps-dump-text --specorder """ "$$SPECORDER" """ - delete_atoms """ "$$DELETE_ATOMS" """ - write fin.lammpstrj --format lammps-dump-text --type_map """ "$$SPECORDER_BASE" """
shell $$AI2KIT_CMD tool ase read ini.data --format lammps-data --style "atomic" - delete_atoms """ "$$DELETE_ATOMS" """ - write fin.data --format lammps-data
''',
    _get_fep_rerun_setting('ini', 'ini.data', 'ini.lammpstrj'),
    _get_fep_rerun_setting('fin', 'fin.data', 'fin.lammpstrj'),
])


PRESET_LAMMPS_INPUT_TEMPLATE = {
    'default': '\n'.join([ _DEFAULT_LAMMPS_TOP, _DP_FORCE_FIELD, _DEFAULT_LAMMPS_BOTTOM]),
    # 2 models fep
    'fep-2m': '\n'.join([ _DEFAULT_LAMMPS_TOP, _DP_FEP_DUAL_FORCE_FIELD, _DEFAULT_LAMMPS_BOTTOM]),
    # 1 model fep
    'fep': '\n'.join([ _DEFAULT_LAMMPS_TOP, _DP_FEP_UNI_FORCE_FIELD, _DEFAULT_LAMMPS_BOTTOM, _FEP_UNI_BOTTOM]),
}
