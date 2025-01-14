# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class DeleteTableColumnsRequest(object):
    _types = {
        "column_start_index": int,
        "column_end_index": int,
    }

    def __init__(self, d=None):
        self.column_start_index: Optional[int] = None
        self.column_end_index: Optional[int] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "DeleteTableColumnsRequestBuilder":
        return DeleteTableColumnsRequestBuilder()


class DeleteTableColumnsRequestBuilder(object):
    def __init__(self) -> None:
        self._delete_table_columns_request = DeleteTableColumnsRequest()

    def column_start_index(self, column_start_index: int) -> "DeleteTableColumnsRequestBuilder":
        self._delete_table_columns_request.column_start_index = column_start_index
        return self

    def column_end_index(self, column_end_index: int) -> "DeleteTableColumnsRequestBuilder":
        self._delete_table_columns_request.column_end_index = column_end_index
        return self

    def build(self) -> "DeleteTableColumnsRequest":
        return self._delete_table_columns_request
