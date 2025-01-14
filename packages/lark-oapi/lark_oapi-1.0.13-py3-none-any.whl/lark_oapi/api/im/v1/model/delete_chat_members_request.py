# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest
from .delete_chat_members_request_body import DeleteChatMembersRequestBody


class DeleteChatMembersRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.member_id_type: Optional[str] = None
        self.chat_id: Optional[str] = None
        self.request_body: Optional[DeleteChatMembersRequestBody] = None

    @staticmethod
    def builder() -> "DeleteChatMembersRequestBuilder":
        return DeleteChatMembersRequestBuilder()


class DeleteChatMembersRequestBuilder(object):

    def __init__(self) -> None:
        delete_chat_members_request = DeleteChatMembersRequest()
        delete_chat_members_request.http_method = HttpMethod.DELETE
        delete_chat_members_request.uri = "/open-apis/im/v1/chats/:chat_id/members"
        delete_chat_members_request.token_types = {AccessTokenType.USER, AccessTokenType.TENANT}
        self._delete_chat_members_request: DeleteChatMembersRequest = delete_chat_members_request

    def member_id_type(self, member_id_type: str) -> "DeleteChatMembersRequestBuilder":
        self._delete_chat_members_request.member_id_type = member_id_type
        self._delete_chat_members_request.add_query("member_id_type", member_id_type)
        return self

    def chat_id(self, chat_id: str) -> "DeleteChatMembersRequestBuilder":
        self._delete_chat_members_request.chat_id = chat_id
        self._delete_chat_members_request.paths["chat_id"] = str(chat_id)
        return self

    def request_body(self, request_body: DeleteChatMembersRequestBody) -> "DeleteChatMembersRequestBuilder":
        self._delete_chat_members_request.request_body = request_body
        self._delete_chat_members_request.body = request_body
        return self

    def build(self) -> DeleteChatMembersRequest:
        return self._delete_chat_members_request
