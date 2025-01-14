# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class UnmergeTableCellsRequest(object):
    _types = {
        "row_index": int,
        "column_index": int,
    }

    def __init__(self, d=None):
        self.row_index: Optional[int] = None
        self.column_index: Optional[int] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "UnmergeTableCellsRequestBuilder":
        return UnmergeTableCellsRequestBuilder()


class UnmergeTableCellsRequestBuilder(object):
    def __init__(self) -> None:
        self._unmerge_table_cells_request = UnmergeTableCellsRequest()

    def row_index(self, row_index: int) -> "UnmergeTableCellsRequestBuilder":
        self._unmerge_table_cells_request.row_index = row_index
        return self

    def column_index(self, column_index: int) -> "UnmergeTableCellsRequestBuilder":
        self._unmerge_table_cells_request.column_index = column_index
        return self

    def build(self) -> "UnmergeTableCellsRequest":
        return self._unmerge_table_cells_request
