"""Root '__init__' of the posggym package."""
# isort: skip_file
# Need to import model and core before other modules
from posggym.model import POSGFullModel, POSGModel
from posggym.core import (
    ActionWrapper,
    Env,
    DefaultEnv,
    ObservationWrapper,
    RewardWrapper,
    Wrapper,
)
from posggym import envs, error, logger, utils, vector, wrappers
from posggym.envs import make, pprint_registry, register, registry, spec


__all__ = [
    # core classes
    "Env",
    "DefaultEnv",
    "Wrapper",
    "ObservationWrapper",
    "ActionWrapper",
    "RewardWrapper",
    "POSGModel",
    "POSGFullModel",
    # registration
    "make",
    "pprint_registry",
    "register",
    "registry",
    "spec",
    # module folders
    "envs",
    "utils",
    "vector",
    "wrappers",
    "error",
    "logger",
]
__version__ = "0.3.2.dev1"
