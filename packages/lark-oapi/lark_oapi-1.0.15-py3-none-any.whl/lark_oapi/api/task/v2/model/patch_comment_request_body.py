# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .input_comment import InputComment


class PatchCommentRequestBody(object):
    _types = {
        "comment": InputComment,
        "update_fields": List[str],
    }

    def __init__(self, d=None):
        self.comment: Optional[InputComment] = None
        self.update_fields: Optional[List[str]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "PatchCommentRequestBodyBuilder":
        return PatchCommentRequestBodyBuilder()


class PatchCommentRequestBodyBuilder(object):
    def __init__(self) -> None:
        self._patch_comment_request_body = PatchCommentRequestBody()

    def comment(self, comment: InputComment) -> "PatchCommentRequestBodyBuilder":
        self._patch_comment_request_body.comment = comment
        return self

    def update_fields(self, update_fields: List[str]) -> "PatchCommentRequestBodyBuilder":
        self._patch_comment_request_body.update_fields = update_fields
        return self

    def build(self) -> "PatchCommentRequestBody":
        return self._patch_comment_request_body
