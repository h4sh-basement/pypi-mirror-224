from collections import defaultdict
from typing import Any
from typing import Dict
from typing import Optional
from typing import Type

from ddtrace.internal import forksafe
from ddtrace.internal.telemetry.constants import TELEMETRY_TYPE_DISTRIBUTION
from ddtrace.internal.telemetry.constants import TELEMETRY_TYPE_GENERATE_METRICS
from ddtrace.internal.telemetry.metrics import DistributionMetric
from ddtrace.internal.telemetry.metrics import Metric
from ddtrace.internal.telemetry.metrics import MetricTagType


NamespaceMetricType = Dict[str, Dict[str, Dict[str, Any]]]


class MetricNamespace:
    def __init__(self):
        # type: () -> None
        self._lock = forksafe.Lock()  # type: forksafe.ResetObject
        self._metrics_data = {
            TELEMETRY_TYPE_GENERATE_METRICS: defaultdict(dict),
            TELEMETRY_TYPE_DISTRIBUTION: defaultdict(dict),
        }  # type: Dict[str, Dict[str, Dict[int, Metric]]]

    def flush(self):
        # type: () -> Dict
        with self._lock:
            namespace_metrics = self._metrics_data
            self._metrics_data = {
                TELEMETRY_TYPE_GENERATE_METRICS: defaultdict(dict),
                TELEMETRY_TYPE_DISTRIBUTION: defaultdict(dict),
            }
            return namespace_metrics

    def add_metric(self, metric_class, namespace, name, value=1.0, tags=None, interval=None):
        # type: (Type[Metric], str, str, float, MetricTagType, Optional[float]) -> None
        """
        Telemetry Metrics are stored in DD dashboards, check the metrics in datadoghq.com/metric/explorer.
        The metric will store in dashboard as "dd.instrumentation_telemetry_data." + namespace + "." + name
        """
        metric_id = Metric.get_id(name, namespace, tags, metric_class.metric_type)
        if metric_class is DistributionMetric:
            metrics_type_payload = TELEMETRY_TYPE_DISTRIBUTION
        else:
            metrics_type_payload = TELEMETRY_TYPE_GENERATE_METRICS

        with self._lock:
            existing_metric = self._metrics_data[metrics_type_payload][namespace].get(metric_id)
            if existing_metric:
                existing_metric.add_point(value)
            else:
                new_metric = metric_class(namespace, name, tags=tags, common=True, interval=interval)
                new_metric.add_point(value)
                self._metrics_data[metrics_type_payload][namespace][metric_id] = new_metric
