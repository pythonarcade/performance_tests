import importlib
import pkgutil
from typing import List, Tuple, Type

from arcade_perf.graph import DataSeries, PerfGraph
from arcade_perf import OUT_DIR
from arcade_perf.tests.base import PerfTest


def find_test_classes(path: str) -> List[Type[PerfTest]]:
    """Find all test classes in submodules"""
    target_module = importlib.import_module(f"arcade_perf.tests.{path}")

    classes = []
    for v in pkgutil.iter_modules(target_module.__path__):
        module = importlib.import_module(f"arcade_perf.tests.{path}.{v.name}")
        if hasattr(module, "Test"):
            classes.append(module.Test)

    return classes


class TestManager:

    def __init__(self, session: str):
        self.session = session
        self.test_classes = find_test_classes("arcade")
        self.test_classes += find_test_classes("pygame")

    def run(self, session_dir):
        """Run all tests"""

        # Run arcade tests first
        for test in self.test_classes:
            test_instance: PerfTest = test()
            test_instance.run(session_dir)

    def create_graph(
        self,
        title: str,
        x_label: str,
        y_label: str,
        series_names = [],
    ):
        """Create a graph using matplotlib"""
        series = []
        for _series in series_names:
            s = DataSeries()
            series.append(s)

    def _filter_tests(self, test_classes, type, name):
        """Filter test classes based on type and name"""
        filtered = []
        for test_cls in test_classes:
            if type and test_cls.type != type:
                continue
            if name and test_cls.name != name:
                continue
            filtered.append(test_cls)

        return filtered
