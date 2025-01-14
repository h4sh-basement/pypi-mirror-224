# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .user import User


class GetUserResponseBody(object):
    _types = {
        "user": User,
    }

    def __init__(self, d=None):
        self.user: Optional[User] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "GetUserResponseBodyBuilder":
        return GetUserResponseBodyBuilder()


class GetUserResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._get_user_response_body = GetUserResponseBody()

    def user(self, user: User) -> "GetUserResponseBodyBuilder":
        self._get_user_response_body.user = user
        return self

    def build(self) -> "GetUserResponseBody":
        return self._get_user_response_body
