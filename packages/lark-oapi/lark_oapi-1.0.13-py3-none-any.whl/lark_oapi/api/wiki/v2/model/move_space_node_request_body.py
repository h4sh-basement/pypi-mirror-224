# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class MoveSpaceNodeRequestBody(object):
    _types = {
        "target_parent_token": str,
        "target_space_id": str,
    }

    def __init__(self, d=None):
        self.target_parent_token: Optional[str] = None
        self.target_space_id: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "MoveSpaceNodeRequestBodyBuilder":
        return MoveSpaceNodeRequestBodyBuilder()


class MoveSpaceNodeRequestBodyBuilder(object):
    def __init__(self) -> None:
        self._move_space_node_request_body = MoveSpaceNodeRequestBody()

    def target_parent_token(self, target_parent_token: str) -> "MoveSpaceNodeRequestBodyBuilder":
        self._move_space_node_request_body.target_parent_token = target_parent_token
        return self

    def target_space_id(self, target_space_id: str) -> "MoveSpaceNodeRequestBodyBuilder":
        self._move_space_node_request_body.target_space_id = target_space_id
        return self

    def build(self) -> "MoveSpaceNodeRequestBody":
        return self._move_space_node_request_body
