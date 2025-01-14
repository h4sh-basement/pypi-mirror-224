# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .space import Space


class CreateSpaceResponseBody(object):
    _types = {
        "space": Space,
    }

    def __init__(self, d=None):
        self.space: Optional[Space] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "CreateSpaceResponseBodyBuilder":
        return CreateSpaceResponseBodyBuilder()


class CreateSpaceResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._create_space_response_body = CreateSpaceResponseBody()

    def space(self, space: Space) -> "CreateSpaceResponseBodyBuilder":
        self._create_space_response_body.space = space
        return self

    def build(self) -> "CreateSpaceResponseBody":
        return self._create_space_response_body
