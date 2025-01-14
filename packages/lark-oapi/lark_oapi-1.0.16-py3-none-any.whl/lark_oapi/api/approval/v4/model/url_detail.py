# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class UrlDetail(object):
    _types = {
        "origin_url": str,
        "url": str,
        "code": str,
        "message": str,
    }

    def __init__(self, d=None):
        self.origin_url: Optional[str] = None
        self.url: Optional[str] = None
        self.code: Optional[str] = None
        self.message: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "UrlDetailBuilder":
        return UrlDetailBuilder()


class UrlDetailBuilder(object):
    def __init__(self) -> None:
        self._url_detail = UrlDetail()

    def origin_url(self, origin_url: str) -> "UrlDetailBuilder":
        self._url_detail.origin_url = origin_url
        return self

    def url(self, url: str) -> "UrlDetailBuilder":
        self._url_detail.url = url
        return self

    def code(self, code: str) -> "UrlDetailBuilder":
        self._url_detail.code = code
        return self

    def message(self, message: str) -> "UrlDetailBuilder":
        self._url_detail.message = message
        return self

    def build(self) -> "UrlDetail":
        return self._url_detail
