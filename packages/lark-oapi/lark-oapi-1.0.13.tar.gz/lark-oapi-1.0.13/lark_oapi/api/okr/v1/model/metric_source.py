# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .metric_unit import MetricUnit


class MetricSource(object):
    _types = {
        "metric_source_id": str,
        "metric_source_name": str,
        "metric_name": str,
        "metric_unit": MetricUnit,
    }

    def __init__(self, d=None):
        self.metric_source_id: Optional[str] = None
        self.metric_source_name: Optional[str] = None
        self.metric_name: Optional[str] = None
        self.metric_unit: Optional[MetricUnit] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "MetricSourceBuilder":
        return MetricSourceBuilder()


class MetricSourceBuilder(object):
    def __init__(self) -> None:
        self._metric_source = MetricSource()

    def metric_source_id(self, metric_source_id: str) -> "MetricSourceBuilder":
        self._metric_source.metric_source_id = metric_source_id
        return self

    def metric_source_name(self, metric_source_name: str) -> "MetricSourceBuilder":
        self._metric_source.metric_source_name = metric_source_name
        return self

    def metric_name(self, metric_name: str) -> "MetricSourceBuilder":
        self._metric_source.metric_name = metric_name
        return self

    def metric_unit(self, metric_unit: MetricUnit) -> "MetricSourceBuilder":
        self._metric_source.metric_unit = metric_unit
        return self

    def build(self) -> "MetricSource":
        return self._metric_source
