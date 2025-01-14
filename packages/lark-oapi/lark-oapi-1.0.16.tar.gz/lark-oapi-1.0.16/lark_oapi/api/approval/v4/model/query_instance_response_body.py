# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .instance_search_item import InstanceSearchItem


class QueryInstanceResponseBody(object):
    _types = {
        "count": int,
        "instance_list": List[InstanceSearchItem],
        "page_token": str,
        "has_more": bool,
    }

    def __init__(self, d=None):
        self.count: Optional[int] = None
        self.instance_list: Optional[List[InstanceSearchItem]] = None
        self.page_token: Optional[str] = None
        self.has_more: Optional[bool] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "QueryInstanceResponseBodyBuilder":
        return QueryInstanceResponseBodyBuilder()


class QueryInstanceResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._query_instance_response_body = QueryInstanceResponseBody()

    def count(self, count: int) -> "QueryInstanceResponseBodyBuilder":
        self._query_instance_response_body.count = count
        return self

    def instance_list(self, instance_list: List[InstanceSearchItem]) -> "QueryInstanceResponseBodyBuilder":
        self._query_instance_response_body.instance_list = instance_list
        return self

    def page_token(self, page_token: str) -> "QueryInstanceResponseBodyBuilder":
        self._query_instance_response_body.page_token = page_token
        return self

    def has_more(self, has_more: bool) -> "QueryInstanceResponseBodyBuilder":
        self._query_instance_response_body.has_more = has_more
        return self

    def build(self) -> "QueryInstanceResponseBody":
        return self._query_instance_response_body
