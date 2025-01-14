# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class Resource(object):
    _types = {
        "type": str,
        "id": str,
    }

    def __init__(self, d=None):
        self.type: Optional[str] = None
        self.id: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ResourceBuilder":
        return ResourceBuilder()


class ResourceBuilder(object):
    def __init__(self) -> None:
        self._resource = Resource()

    def type(self, type: str) -> "ResourceBuilder":
        self._resource.type = type
        return self

    def id(self, id: str) -> "ResourceBuilder":
        self._resource.id = id
        return self

    def build(self) -> "Resource":
        return self._resource
