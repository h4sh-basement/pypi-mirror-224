# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .job_title import JobTitle


class ListJobTitleResponseBody(object):
    _types = {
        "items": List[JobTitle],
        "page_token": str,
        "has_more": bool,
    }

    def __init__(self, d=None):
        self.items: Optional[List[JobTitle]] = None
        self.page_token: Optional[str] = None
        self.has_more: Optional[bool] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ListJobTitleResponseBodyBuilder":
        return ListJobTitleResponseBodyBuilder()


class ListJobTitleResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._list_job_title_response_body = ListJobTitleResponseBody()

    def items(self, items: List[JobTitle]) -> "ListJobTitleResponseBodyBuilder":
        self._list_job_title_response_body.items = items
        return self

    def page_token(self, page_token: str) -> "ListJobTitleResponseBodyBuilder":
        self._list_job_title_response_body.page_token = page_token
        return self

    def has_more(self, has_more: bool) -> "ListJobTitleResponseBodyBuilder":
        self._list_job_title_response_body.has_more = has_more
        return self

    def build(self) -> "ListJobTitleResponseBody":
        return self._list_job_title_response_body
