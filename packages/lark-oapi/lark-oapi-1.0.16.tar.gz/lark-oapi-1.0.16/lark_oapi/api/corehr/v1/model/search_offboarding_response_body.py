# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .offboarding import Offboarding


class SearchOffboardingResponseBody(object):
    _types = {
        "items": List[Offboarding],
        "page_token": str,
        "has_more": bool,
    }

    def __init__(self, d=None):
        self.items: Optional[List[Offboarding]] = None
        self.page_token: Optional[str] = None
        self.has_more: Optional[bool] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "SearchOffboardingResponseBodyBuilder":
        return SearchOffboardingResponseBodyBuilder()


class SearchOffboardingResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._search_offboarding_response_body = SearchOffboardingResponseBody()

    def items(self, items: List[Offboarding]) -> "SearchOffboardingResponseBodyBuilder":
        self._search_offboarding_response_body.items = items
        return self

    def page_token(self, page_token: str) -> "SearchOffboardingResponseBodyBuilder":
        self._search_offboarding_response_body.page_token = page_token
        return self

    def has_more(self, has_more: bool) -> "SearchOffboardingResponseBodyBuilder":
        self._search_offboarding_response_body.has_more = has_more
        return self

    def build(self) -> "SearchOffboardingResponseBody":
        return self._search_offboarding_response_body
