# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class CopySpaceNodeRequestBody(object):
    _types = {
        "target_parent_token": str,
        "target_space_id": int,
        "title": str,
    }

    def __init__(self, d=None):
        self.target_parent_token: Optional[str] = None
        self.target_space_id: Optional[int] = None
        self.title: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "CopySpaceNodeRequestBodyBuilder":
        return CopySpaceNodeRequestBodyBuilder()


class CopySpaceNodeRequestBodyBuilder(object):
    def __init__(self) -> None:
        self._copy_space_node_request_body = CopySpaceNodeRequestBody()

    def target_parent_token(self, target_parent_token: str) -> "CopySpaceNodeRequestBodyBuilder":
        self._copy_space_node_request_body.target_parent_token = target_parent_token
        return self

    def target_space_id(self, target_space_id: int) -> "CopySpaceNodeRequestBodyBuilder":
        self._copy_space_node_request_body.target_space_id = target_space_id
        return self

    def title(self, title: str) -> "CopySpaceNodeRequestBodyBuilder":
        self._copy_space_node_request_body.title = title
        return self

    def build(self) -> "CopySpaceNodeRequestBody":
        return self._copy_space_node_request_body
