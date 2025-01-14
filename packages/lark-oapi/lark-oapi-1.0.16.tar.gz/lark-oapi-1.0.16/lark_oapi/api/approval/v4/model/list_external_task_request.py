# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest
from .list_external_task_request_body import ListExternalTaskRequestBody


class ListExternalTaskRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.page_size: Optional[int] = None
        self.page_token: Optional[str] = None
        self.request_body: Optional[ListExternalTaskRequestBody] = None

    @staticmethod
    def builder() -> "ListExternalTaskRequestBuilder":
        return ListExternalTaskRequestBuilder()


class ListExternalTaskRequestBuilder(object):

    def __init__(self) -> None:
        list_external_task_request = ListExternalTaskRequest()
        list_external_task_request.http_method = HttpMethod.GET
        list_external_task_request.uri = "/open-apis/approval/v4/external_tasks"
        list_external_task_request.token_types = {AccessTokenType.TENANT}
        self._list_external_task_request: ListExternalTaskRequest = list_external_task_request

    def page_size(self, page_size: int) -> "ListExternalTaskRequestBuilder":
        self._list_external_task_request.page_size = page_size
        self._list_external_task_request.add_query("page_size", page_size)
        return self

    def page_token(self, page_token: str) -> "ListExternalTaskRequestBuilder":
        self._list_external_task_request.page_token = page_token
        self._list_external_task_request.add_query("page_token", page_token)
        return self

    def request_body(self, request_body: ListExternalTaskRequestBody) -> "ListExternalTaskRequestBuilder":
        self._list_external_task_request.request_body = request_body
        self._list_external_task_request.body = request_body
        return self

    def build(self) -> ListExternalTaskRequest:
        return self._list_external_task_request
