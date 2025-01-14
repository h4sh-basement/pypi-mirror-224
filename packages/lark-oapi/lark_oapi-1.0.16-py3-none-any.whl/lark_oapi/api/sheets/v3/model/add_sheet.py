# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class AddSheet(object):
    _types = {
        "title": str,
        "index": int,
    }

    def __init__(self, d=None):
        self.title: Optional[str] = None
        self.index: Optional[int] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "AddSheetBuilder":
        return AddSheetBuilder()


class AddSheetBuilder(object):
    def __init__(self) -> None:
        self._add_sheet = AddSheet()

    def title(self, title: str) -> "AddSheetBuilder":
        self._add_sheet.title = title
        return self

    def index(self, index: int) -> "AddSheetBuilder":
        self._add_sheet.index = index
        return self

    def build(self) -> "AddSheet":
        return self._add_sheet
