# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .message import Message


class ListMessageResponseBody(object):
    _types = {
        "has_more": bool,
        "page_token": str,
        "items": List[Message],
    }

    def __init__(self, d=None):
        self.has_more: Optional[bool] = None
        self.page_token: Optional[str] = None
        self.items: Optional[List[Message]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ListMessageResponseBodyBuilder":
        return ListMessageResponseBodyBuilder()


class ListMessageResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._list_message_response_body = ListMessageResponseBody()

    def has_more(self, has_more: bool) -> "ListMessageResponseBodyBuilder":
        self._list_message_response_body.has_more = has_more
        return self

    def page_token(self, page_token: str) -> "ListMessageResponseBodyBuilder":
        self._list_message_response_body.page_token = page_token
        return self

    def items(self, items: List[Message]) -> "ListMessageResponseBodyBuilder":
        self._list_message_response_body.items = items
        return self

    def build(self) -> "ListMessageResponseBody":
        return self._list_message_response_body
