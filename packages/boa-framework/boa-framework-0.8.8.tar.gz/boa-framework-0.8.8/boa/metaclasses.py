"""
########################
Meta Classes
########################

Meta class modify class behaviors. For example, the :class:`.WrapperRegister` ensures that all subclasses of
:class:`.BaseWrapper` will wrap functions in :func:`.cd_and_cd_back_dec`
to make sure that if users do any directory changes inside a wrapper function,
the original directory is returned to afterwards.

"""
import sys
from abc import ABCMeta
from functools import wraps
from pathlib import Path

from ax.storage.json_store.registry import CORE_DECODER_REGISTRY, CORE_ENCODER_REGISTRY
from ax.storage.metric_registry import CORE_METRIC_REGISTRY
from ax.storage.runner_registry import CORE_RUNNER_REGISTRY

from boa.logger import get_logger
from boa.wrappers.wrapper_utils import cd_and_cd_back_dec

logger = get_logger()


def write_exception_to_log(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            logger.exception(f"Boa Wrapper encountered Exception: {e!r} in %s", func.__name__)
            raise

    return wrapper


class WrapperRegister(ABCMeta):
    def __init__(cls, *args, **kwargs):
        cls.load_config = write_exception_to_log(cd_and_cd_back_dec()(cls.load_config))
        cls.mk_experiment_dir = write_exception_to_log(cd_and_cd_back_dec()(cls.mk_experiment_dir))
        cls.write_configs = write_exception_to_log(cd_and_cd_back_dec()(cls.write_configs))
        cls.run_model = write_exception_to_log(cd_and_cd_back_dec()(cls.run_model))
        cls.set_trial_status = write_exception_to_log(cd_and_cd_back_dec()(cls.set_trial_status))
        cls.fetch_trial_data = write_exception_to_log(cd_and_cd_back_dec()(cls.fetch_trial_data))
        cls._fetch_trial_data = write_exception_to_log(cd_and_cd_back_dec()(cls._fetch_trial_data))
        try:
            _path = Path(sys.modules[cls.__module__].__file__)
        except AttributeError:  # running in a jupyter notebook `__file__` doesn't work
            logger.warning(
                "Could not save Wrapper file location. "
                "\nIs your Wrapper defined in a Jupyter Notebook?"
                "\nBOA will not be able to reload from file without directly"
                "\nreinstantiating your Wrapper and passing it to BOA"
            )
            _path = None
        cls._path = _path
        super().__init__(*args, **kwargs)


class RunnerRegister(ABCMeta):
    def __init__(cls, *args, **kwargs):
        CORE_ENCODER_REGISTRY[cls] = cls.to_dict
        CORE_DECODER_REGISTRY[cls.__name__] = cls
        next_pk = max(CORE_RUNNER_REGISTRY.values()) + 1
        CORE_RUNNER_REGISTRY[cls] = next_pk


class MetricRegister(ABCMeta):
    def __init__(cls, *args, **kwargs):
        CORE_ENCODER_REGISTRY[cls] = cls.to_dict
        CORE_DECODER_REGISTRY[cls.__name__] = cls
        next_pk = max(CORE_METRIC_REGISTRY.values()) + 1
        CORE_METRIC_REGISTRY[cls] = next_pk
