import importlib
from typing import List
from typing import Optional
from typing import Set
from typing import Tuple

from ..logger import get_logger


log = get_logger(__name__)


class ValueCollector(object):
    """A basic state machine useful for collecting, caching and updating data
    obtained from different Python modules.

    The two primary use-cases are
    1) data loaded once (like tagging information)
    2) periodically updating data sources (like thread count)

    Functionality is provided for requiring and importing modules which may or
    may not be installed.
    """

    enabled = True
    periodic = False
    required_modules = []  # type: List[str]
    value = None  # type: Optional[List[Tuple[str, str]]]
    value_loaded = False

    def __init__(self, enabled=None, periodic=None, required_modules=None):
        # type: (Optional[bool], Optional[bool], Optional[List[str]]) -> None
        self.enabled = self.enabled if enabled is None else enabled
        self.periodic = self.periodic if periodic is None else periodic
        self.required_modules = self.required_modules if required_modules is None else required_modules

        self._modules_successfully_loaded = False
        self.modules = self._load_modules()
        if self._modules_successfully_loaded:
            self._on_modules_load()

    def _on_modules_load(self):
        """Hook triggered after all required_modules have been successfully loaded."""

    def _load_modules(self):
        modules = {}
        try:
            for module in self.required_modules:
                modules[module] = importlib.import_module(module)
            self._modules_successfully_loaded = True
        except ImportError:
            # DEV: disable collector if we cannot load any of the required modules
            self.enabled = False
            log.warning('Could not import module "%s" for %s. Disabling collector.', module, self)
            return None
        return modules

    def collect(self, keys=None):
        # type: (Optional[Set[str]]) -> Optional[List[Tuple[str, str]]]
        """Returns metrics as collected by `collect_fn`.

        :param keys: The keys of the metrics to collect.
        """
        if not self.enabled:
            return self.value

        keys = keys or set()

        if not self.periodic and self.value_loaded:
            return self.value

        # call underlying collect function and filter out keys not requested
        # TODO: provide base method collect_fn() in ValueCollector
        self.value = self.collect_fn(keys)  # type: ignore[attr-defined]

        # filter values for keys
        if len(keys) > 0 and isinstance(self.value, list):
            self.value = [(k, v) for (k, v) in self.value if k in keys]

        self.value_loaded = True
        return self.value

    def __repr__(self):
        return "<{}(enabled={},periodic={},required_modules={})>".format(
            self.__class__.__name__,
            self.enabled,
            self.periodic,
            self.required_modules,
        )
