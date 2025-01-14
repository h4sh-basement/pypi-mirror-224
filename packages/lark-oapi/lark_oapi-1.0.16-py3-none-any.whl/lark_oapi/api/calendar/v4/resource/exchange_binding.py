# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core import JSON
from lark_oapi.core.const import UTF_8
from lark_oapi.core.http import Transport
from lark_oapi.core.model import Config, RequestOption, RawResponse
from lark_oapi.core.token import verify
from ..model.create_exchange_binding_request import CreateExchangeBindingRequest
from ..model.create_exchange_binding_response import CreateExchangeBindingResponse
from ..model.delete_exchange_binding_request import DeleteExchangeBindingRequest
from ..model.delete_exchange_binding_response import DeleteExchangeBindingResponse
from ..model.get_exchange_binding_request import GetExchangeBindingRequest
from ..model.get_exchange_binding_response import GetExchangeBindingResponse


class ExchangeBinding(object):
    def __init__(self, config: Config) -> None:
        self.config: Config = config

    def create(self, request: CreateExchangeBindingRequest,
               option: Optional[RequestOption] = None) -> CreateExchangeBindingResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: CreateExchangeBindingResponse = JSON.unmarshal(str(resp.content, UTF_8),
                                                                 CreateExchangeBindingResponse)
        response.raw = resp

        return response

    def delete(self, request: DeleteExchangeBindingRequest,
               option: Optional[RequestOption] = None) -> DeleteExchangeBindingResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: DeleteExchangeBindingResponse = JSON.unmarshal(str(resp.content, UTF_8),
                                                                 DeleteExchangeBindingResponse)
        response.raw = resp

        return response

    def get(self, request: GetExchangeBindingRequest,
            option: Optional[RequestOption] = None) -> GetExchangeBindingResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: GetExchangeBindingResponse = JSON.unmarshal(str(resp.content, UTF_8), GetExchangeBindingResponse)
        response.raw = resp

        return response
