# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest


class MeJoinChatMembersRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.chat_id: Optional[str] = None

    @staticmethod
    def builder() -> "MeJoinChatMembersRequestBuilder":
        return MeJoinChatMembersRequestBuilder()


class MeJoinChatMembersRequestBuilder(object):

    def __init__(self) -> None:
        me_join_chat_members_request = MeJoinChatMembersRequest()
        me_join_chat_members_request.http_method = HttpMethod.PATCH
        me_join_chat_members_request.uri = "/open-apis/im/v1/chats/:chat_id/members/me_join"
        me_join_chat_members_request.token_types = {AccessTokenType.USER, AccessTokenType.TENANT}
        self._me_join_chat_members_request: MeJoinChatMembersRequest = me_join_chat_members_request

    def chat_id(self, chat_id: str) -> "MeJoinChatMembersRequestBuilder":
        self._me_join_chat_members_request.chat_id = chat_id
        self._me_join_chat_members_request.paths["chat_id"] = str(chat_id)
        return self

    def build(self) -> MeJoinChatMembersRequest:
        return self._me_join_chat_members_request
