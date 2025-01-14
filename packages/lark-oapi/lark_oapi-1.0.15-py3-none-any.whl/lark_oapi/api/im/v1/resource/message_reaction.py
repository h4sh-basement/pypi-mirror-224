# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core import JSON
from lark_oapi.core.const import UTF_8
from lark_oapi.core.http import Transport
from lark_oapi.core.model import Config, RequestOption, RawResponse
from lark_oapi.core.token import verify
from ..model.create_message_reaction_request import CreateMessageReactionRequest
from ..model.create_message_reaction_response import CreateMessageReactionResponse
from ..model.delete_message_reaction_request import DeleteMessageReactionRequest
from ..model.delete_message_reaction_response import DeleteMessageReactionResponse
from ..model.list_message_reaction_request import ListMessageReactionRequest
from ..model.list_message_reaction_response import ListMessageReactionResponse


class MessageReaction(object):
    def __init__(self, config: Config) -> None:
        self.config: Config = config

    def create(self, request: CreateMessageReactionRequest,
               option: Optional[RequestOption] = None) -> CreateMessageReactionResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: CreateMessageReactionResponse = JSON.unmarshal(str(resp.content, UTF_8),
                                                                 CreateMessageReactionResponse)
        response.raw = resp

        return response

    def delete(self, request: DeleteMessageReactionRequest,
               option: Optional[RequestOption] = None) -> DeleteMessageReactionResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: DeleteMessageReactionResponse = JSON.unmarshal(str(resp.content, UTF_8),
                                                                 DeleteMessageReactionResponse)
        response.raw = resp

        return response

    def list(self, request: ListMessageReactionRequest,
             option: Optional[RequestOption] = None) -> ListMessageReactionResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: ListMessageReactionResponse = JSON.unmarshal(str(resp.content, UTF_8), ListMessageReactionResponse)
        response.raw = resp

        return response
