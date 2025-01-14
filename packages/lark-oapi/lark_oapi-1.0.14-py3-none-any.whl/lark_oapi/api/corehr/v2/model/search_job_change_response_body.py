# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .job_change import JobChange


class SearchJobChangeResponseBody(object):
    _types = {
        "items": List[JobChange],
        "has_more": bool,
        "page_token": str,
    }

    def __init__(self, d=None):
        self.items: Optional[List[JobChange]] = None
        self.has_more: Optional[bool] = None
        self.page_token: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "SearchJobChangeResponseBodyBuilder":
        return SearchJobChangeResponseBodyBuilder()


class SearchJobChangeResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._search_job_change_response_body = SearchJobChangeResponseBody()

    def items(self, items: List[JobChange]) -> "SearchJobChangeResponseBodyBuilder":
        self._search_job_change_response_body.items = items
        return self

    def has_more(self, has_more: bool) -> "SearchJobChangeResponseBodyBuilder":
        self._search_job_change_response_body.has_more = has_more
        return self

    def page_token(self, page_token: str) -> "SearchJobChangeResponseBodyBuilder":
        self._search_job_change_response_body.page_token = page_token
        return self

    def build(self) -> "SearchJobChangeResponseBody":
        return self._search_job_change_response_body
