# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core import JSON
from lark_oapi.core.const import UTF_8
from lark_oapi.core.http import Transport
from lark_oapi.core.model import Config, RequestOption, RawResponse
from lark_oapi.core.token import verify
from ..model.resend_app_ticket_request import ResendAppTicketRequest
from ..model.resend_app_ticket_response import ResendAppTicketResponse


class AppTicket(object):
    def __init__(self, config: Config) -> None:
        self.config: Config = config

    def resend(self, request: ResendAppTicketRequest,
               option: Optional[RequestOption] = None) -> ResendAppTicketResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: ResendAppTicketResponse = JSON.unmarshal(str(resp.content, UTF_8), ResendAppTicketResponse)
        response.raw = resp

        return response
