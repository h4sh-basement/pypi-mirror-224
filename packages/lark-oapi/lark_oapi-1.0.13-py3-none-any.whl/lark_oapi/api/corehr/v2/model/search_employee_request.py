# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest
from .search_employee_request_body import SearchEmployeeRequestBody


class SearchEmployeeRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.page_size: Optional[int] = None
        self.page_token: Optional[str] = None
        self.user_id_type: Optional[str] = None
        self.department_id_type: Optional[str] = None
        self.request_body: Optional[SearchEmployeeRequestBody] = None

    @staticmethod
    def builder() -> "SearchEmployeeRequestBuilder":
        return SearchEmployeeRequestBuilder()


class SearchEmployeeRequestBuilder(object):

    def __init__(self) -> None:
        search_employee_request = SearchEmployeeRequest()
        search_employee_request.http_method = HttpMethod.POST
        search_employee_request.uri = "/open-apis/corehr/v2/employees/search"
        search_employee_request.token_types = {AccessTokenType.TENANT}
        self._search_employee_request: SearchEmployeeRequest = search_employee_request

    def page_size(self, page_size: int) -> "SearchEmployeeRequestBuilder":
        self._search_employee_request.page_size = page_size
        self._search_employee_request.add_query("page_size", page_size)
        return self

    def page_token(self, page_token: str) -> "SearchEmployeeRequestBuilder":
        self._search_employee_request.page_token = page_token
        self._search_employee_request.add_query("page_token", page_token)
        return self

    def user_id_type(self, user_id_type: str) -> "SearchEmployeeRequestBuilder":
        self._search_employee_request.user_id_type = user_id_type
        self._search_employee_request.add_query("user_id_type", user_id_type)
        return self

    def department_id_type(self, department_id_type: str) -> "SearchEmployeeRequestBuilder":
        self._search_employee_request.department_id_type = department_id_type
        self._search_employee_request.add_query("department_id_type", department_id_type)
        return self

    def request_body(self, request_body: SearchEmployeeRequestBody) -> "SearchEmployeeRequestBuilder":
        self._search_employee_request.request_body = request_body
        self._search_employee_request.body = request_body
        return self

    def build(self) -> SearchEmployeeRequest:
        return self._search_employee_request
