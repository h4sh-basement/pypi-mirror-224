# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class PatchFileSubscriptionRequestBody(object):
    _types = {
        "is_subscribe": bool,
        "file_type": str,
    }

    def __init__(self, d=None):
        self.is_subscribe: Optional[bool] = None
        self.file_type: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "PatchFileSubscriptionRequestBodyBuilder":
        return PatchFileSubscriptionRequestBodyBuilder()


class PatchFileSubscriptionRequestBodyBuilder(object):
    def __init__(self) -> None:
        self._patch_file_subscription_request_body = PatchFileSubscriptionRequestBody()

    def is_subscribe(self, is_subscribe: bool) -> "PatchFileSubscriptionRequestBodyBuilder":
        self._patch_file_subscription_request_body.is_subscribe = is_subscribe
        return self

    def file_type(self, file_type: str) -> "PatchFileSubscriptionRequestBodyBuilder":
        self._patch_file_subscription_request_body.file_type = file_type
        return self

    def build(self) -> "PatchFileSubscriptionRequestBody":
        return self._patch_file_subscription_request_body
