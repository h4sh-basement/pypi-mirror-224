# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core import JSON
from lark_oapi.core.const import UTF_8
from lark_oapi.core.http import Transport
from lark_oapi.core.model import Config, RequestOption, RawResponse
from lark_oapi.core.token import verify
from ..model.create_offer_request import CreateOfferRequest
from ..model.create_offer_response import CreateOfferResponse
from ..model.get_offer_request import GetOfferRequest
from ..model.get_offer_response import GetOfferResponse
from ..model.intern_offer_status_offer_request import InternOfferStatusOfferRequest
from ..model.intern_offer_status_offer_response import InternOfferStatusOfferResponse
from ..model.list_offer_request import ListOfferRequest
from ..model.list_offer_response import ListOfferResponse
from ..model.offer_status_offer_request import OfferStatusOfferRequest
from ..model.offer_status_offer_response import OfferStatusOfferResponse
from ..model.update_offer_request import UpdateOfferRequest
from ..model.update_offer_response import UpdateOfferResponse


class Offer(object):
    def __init__(self, config: Config) -> None:
        self.config: Config = config

    def create(self, request: CreateOfferRequest, option: Optional[RequestOption] = None) -> CreateOfferResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: CreateOfferResponse = JSON.unmarshal(str(resp.content, UTF_8), CreateOfferResponse)
        response.raw = resp

        return response

    def get(self, request: GetOfferRequest, option: Optional[RequestOption] = None) -> GetOfferResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: GetOfferResponse = JSON.unmarshal(str(resp.content, UTF_8), GetOfferResponse)
        response.raw = resp

        return response

    def intern_offer_status(self, request: InternOfferStatusOfferRequest,
                            option: Optional[RequestOption] = None) -> InternOfferStatusOfferResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: InternOfferStatusOfferResponse = JSON.unmarshal(str(resp.content, UTF_8),
                                                                  InternOfferStatusOfferResponse)
        response.raw = resp

        return response

    def list(self, request: ListOfferRequest, option: Optional[RequestOption] = None) -> ListOfferResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: ListOfferResponse = JSON.unmarshal(str(resp.content, UTF_8), ListOfferResponse)
        response.raw = resp

        return response

    def offer_status(self, request: OfferStatusOfferRequest,
                     option: Optional[RequestOption] = None) -> OfferStatusOfferResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: OfferStatusOfferResponse = JSON.unmarshal(str(resp.content, UTF_8), OfferStatusOfferResponse)
        response.raw = resp

        return response

    def update(self, request: UpdateOfferRequest, option: Optional[RequestOption] = None) -> UpdateOfferResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: UpdateOfferResponse = JSON.unmarshal(str(resp.content, UTF_8), UpdateOfferResponse)
        response.raw = resp

        return response
