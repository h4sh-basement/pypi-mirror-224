# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class CreateAppTableResponseBody(object):
    _types = {
        "table_id": str,
        "default_view_id": str,
        "field_id_list": List[str],
    }

    def __init__(self, d=None):
        self.table_id: Optional[str] = None
        self.default_view_id: Optional[str] = None
        self.field_id_list: Optional[List[str]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "CreateAppTableResponseBodyBuilder":
        return CreateAppTableResponseBodyBuilder()


class CreateAppTableResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._create_app_table_response_body = CreateAppTableResponseBody()

    def table_id(self, table_id: str) -> "CreateAppTableResponseBodyBuilder":
        self._create_app_table_response_body.table_id = table_id
        return self

    def default_view_id(self, default_view_id: str) -> "CreateAppTableResponseBodyBuilder":
        self._create_app_table_response_body.default_view_id = default_view_id
        return self

    def field_id_list(self, field_id_list: List[str]) -> "CreateAppTableResponseBodyBuilder":
        self._create_app_table_response_body.field_id_list = field_id_list
        return self

    def build(self) -> "CreateAppTableResponseBody":
        return self._create_app_table_response_body
