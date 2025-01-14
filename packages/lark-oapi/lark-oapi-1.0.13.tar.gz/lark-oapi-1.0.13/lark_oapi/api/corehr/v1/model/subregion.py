# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .i18n import I18n


class Subregion(object):
    _types = {
        "id": str,
        "name": List[I18n],
        "subdivision_id": str,
        "superior_subregion_id": str,
    }

    def __init__(self, d=None):
        self.id: Optional[str] = None
        self.name: Optional[List[I18n]] = None
        self.subdivision_id: Optional[str] = None
        self.superior_subregion_id: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "SubregionBuilder":
        return SubregionBuilder()


class SubregionBuilder(object):
    def __init__(self) -> None:
        self._subregion = Subregion()

    def id(self, id: str) -> "SubregionBuilder":
        self._subregion.id = id
        return self

    def name(self, name: List[I18n]) -> "SubregionBuilder":
        self._subregion.name = name
        return self

    def subdivision_id(self, subdivision_id: str) -> "SubregionBuilder":
        self._subregion.subdivision_id = subdivision_id
        return self

    def superior_subregion_id(self, superior_subregion_id: str) -> "SubregionBuilder":
        self._subregion.superior_subregion_id = superior_subregion_id
        return self

    def build(self) -> "Subregion":
        return self._subregion
