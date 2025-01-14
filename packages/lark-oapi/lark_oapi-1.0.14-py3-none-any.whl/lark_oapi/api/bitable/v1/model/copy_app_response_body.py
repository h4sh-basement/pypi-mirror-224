# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .app import App


class CopyAppResponseBody(object):
    _types = {
        "app": App,
    }

    def __init__(self, d=None):
        self.app: Optional[App] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "CopyAppResponseBodyBuilder":
        return CopyAppResponseBodyBuilder()


class CopyAppResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._copy_app_response_body = CopyAppResponseBody()

    def app(self, app: App) -> "CopyAppResponseBodyBuilder":
        self._copy_app_response_body.app = app
        return self

    def build(self) -> "CopyAppResponseBody":
        return self._copy_app_response_body
