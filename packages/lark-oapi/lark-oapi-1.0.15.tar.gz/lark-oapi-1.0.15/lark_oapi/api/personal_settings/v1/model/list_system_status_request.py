# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest


class ListSystemStatusRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.page_size: Optional[int] = None
        self.page_token: Optional[str] = None

    @staticmethod
    def builder() -> "ListSystemStatusRequestBuilder":
        return ListSystemStatusRequestBuilder()


class ListSystemStatusRequestBuilder(object):

    def __init__(self) -> None:
        list_system_status_request = ListSystemStatusRequest()
        list_system_status_request.http_method = HttpMethod.GET
        list_system_status_request.uri = "/open-apis/personal_settings/v1/system_statuses"
        list_system_status_request.token_types = {AccessTokenType.TENANT}
        self._list_system_status_request: ListSystemStatusRequest = list_system_status_request

    def page_size(self, page_size: int) -> "ListSystemStatusRequestBuilder":
        self._list_system_status_request.page_size = page_size
        self._list_system_status_request.add_query("page_size", page_size)
        return self

    def page_token(self, page_token: str) -> "ListSystemStatusRequestBuilder":
        self._list_system_status_request.page_token = page_token
        self._list_system_status_request.add_query("page_token", page_token)
        return self

    def build(self) -> ListSystemStatusRequest:
        return self._list_system_status_request
