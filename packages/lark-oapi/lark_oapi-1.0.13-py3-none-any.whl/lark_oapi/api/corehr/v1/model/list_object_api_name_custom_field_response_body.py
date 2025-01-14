# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .object import Object


class ListObjectApiNameCustomFieldResponseBody(object):
    _types = {
        "items": List[Object],
        "has_more": bool,
        "page_token": str,
    }

    def __init__(self, d=None):
        self.items: Optional[List[Object]] = None
        self.has_more: Optional[bool] = None
        self.page_token: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ListObjectApiNameCustomFieldResponseBodyBuilder":
        return ListObjectApiNameCustomFieldResponseBodyBuilder()


class ListObjectApiNameCustomFieldResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._list_object_api_name_custom_field_response_body = ListObjectApiNameCustomFieldResponseBody()

    def items(self, items: List[Object]) -> "ListObjectApiNameCustomFieldResponseBodyBuilder":
        self._list_object_api_name_custom_field_response_body.items = items
        return self

    def has_more(self, has_more: bool) -> "ListObjectApiNameCustomFieldResponseBodyBuilder":
        self._list_object_api_name_custom_field_response_body.has_more = has_more
        return self

    def page_token(self, page_token: str) -> "ListObjectApiNameCustomFieldResponseBodyBuilder":
        self._list_object_api_name_custom_field_response_body.page_token = page_token
        return self

    def build(self) -> "ListObjectApiNameCustomFieldResponseBody":
        return self._list_object_api_name_custom_field_response_body
