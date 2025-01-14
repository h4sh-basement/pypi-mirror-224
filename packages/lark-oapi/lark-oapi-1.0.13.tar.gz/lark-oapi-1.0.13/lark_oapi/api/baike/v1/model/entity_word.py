# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class EntityWord(object):
    _types = {
        "name": str,
        "aliases": List[str],
    }

    def __init__(self, d=None):
        self.name: Optional[str] = None
        self.aliases: Optional[List[str]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "EntityWordBuilder":
        return EntityWordBuilder()


class EntityWordBuilder(object):
    def __init__(self) -> None:
        self._entity_word = EntityWord()

    def name(self, name: str) -> "EntityWordBuilder":
        self._entity_word.name = name
        return self

    def aliases(self, aliases: List[str]) -> "EntityWordBuilder":
        self._entity_word.aliases = aliases
        return self

    def build(self) -> "EntityWord":
        return self._entity_word
