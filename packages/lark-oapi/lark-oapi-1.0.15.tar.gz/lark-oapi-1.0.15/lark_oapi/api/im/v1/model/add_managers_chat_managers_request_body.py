# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class AddManagersChatManagersRequestBody(object):
    _types = {
        "manager_ids": List[str],
    }

    def __init__(self, d=None):
        self.manager_ids: Optional[List[str]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "AddManagersChatManagersRequestBodyBuilder":
        return AddManagersChatManagersRequestBodyBuilder()


class AddManagersChatManagersRequestBodyBuilder(object):
    def __init__(self) -> None:
        self._add_managers_chat_managers_request_body = AddManagersChatManagersRequestBody()

    def manager_ids(self, manager_ids: List[str]) -> "AddManagersChatManagersRequestBodyBuilder":
        self._add_managers_chat_managers_request_body.manager_ids = manager_ids
        return self

    def build(self) -> "AddManagersChatManagersRequestBody":
        return self._add_managers_chat_managers_request_body
