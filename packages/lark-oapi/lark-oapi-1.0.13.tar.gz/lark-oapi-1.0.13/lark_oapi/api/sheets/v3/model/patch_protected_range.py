# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .protected_columns import ProtectedColumns
from .protected_rows import ProtectedRows


class PatchProtectedRange(object):
    _types = {
        "description": str,
        "protected_rows": ProtectedRows,
        "protected_columns": ProtectedColumns,
    }

    def __init__(self, d=None):
        self.description: Optional[str] = None
        self.protected_rows: Optional[ProtectedRows] = None
        self.protected_columns: Optional[ProtectedColumns] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "PatchProtectedRangeBuilder":
        return PatchProtectedRangeBuilder()


class PatchProtectedRangeBuilder(object):
    def __init__(self) -> None:
        self._patch_protected_range = PatchProtectedRange()

    def description(self, description: str) -> "PatchProtectedRangeBuilder":
        self._patch_protected_range.description = description
        return self

    def protected_rows(self, protected_rows: ProtectedRows) -> "PatchProtectedRangeBuilder":
        self._patch_protected_range.protected_rows = protected_rows
        return self

    def protected_columns(self, protected_columns: ProtectedColumns) -> "PatchProtectedRangeBuilder":
        self._patch_protected_range.protected_columns = protected_columns
        return self

    def build(self) -> "PatchProtectedRange":
        return self._patch_protected_range
