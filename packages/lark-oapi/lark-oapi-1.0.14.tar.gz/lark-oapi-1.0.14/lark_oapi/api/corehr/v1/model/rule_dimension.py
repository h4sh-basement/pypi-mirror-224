# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .name import Name


class RuleDimension(object):
    _types = {
        "entity_key": str,
        "entity_name": Name,
    }

    def __init__(self, d=None):
        self.entity_key: Optional[str] = None
        self.entity_name: Optional[Name] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "RuleDimensionBuilder":
        return RuleDimensionBuilder()


class RuleDimensionBuilder(object):
    def __init__(self) -> None:
        self._rule_dimension = RuleDimension()

    def entity_key(self, entity_key: str) -> "RuleDimensionBuilder":
        self._rule_dimension.entity_key = entity_key
        return self

    def entity_name(self, entity_name: Name) -> "RuleDimensionBuilder":
        self._rule_dimension.entity_name = entity_name
        return self

    def build(self) -> "RuleDimension":
        return self._rule_dimension
