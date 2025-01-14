# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .metric_source import MetricSource


class ListMetricSourceResponseBody(object):
    _types = {
        "total": int,
        "has_more": bool,
        "page_token": str,
        "items": List[MetricSource],
    }

    def __init__(self, d=None):
        self.total: Optional[int] = None
        self.has_more: Optional[bool] = None
        self.page_token: Optional[str] = None
        self.items: Optional[List[MetricSource]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ListMetricSourceResponseBodyBuilder":
        return ListMetricSourceResponseBodyBuilder()


class ListMetricSourceResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._list_metric_source_response_body = ListMetricSourceResponseBody()

    def total(self, total: int) -> "ListMetricSourceResponseBodyBuilder":
        self._list_metric_source_response_body.total = total
        return self

    def has_more(self, has_more: bool) -> "ListMetricSourceResponseBodyBuilder":
        self._list_metric_source_response_body.has_more = has_more
        return self

    def page_token(self, page_token: str) -> "ListMetricSourceResponseBodyBuilder":
        self._list_metric_source_response_body.page_token = page_token
        return self

    def items(self, items: List[MetricSource]) -> "ListMetricSourceResponseBodyBuilder":
        self._list_metric_source_response_body.items = items
        return self

    def build(self) -> "ListMetricSourceResponseBody":
        return self._list_metric_source_response_body
