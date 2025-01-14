# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class UserContactInfo(object):
    _types = {
        "user_id": str,
        "mobile": str,
        "email": str,
    }

    def __init__(self, d=None):
        self.user_id: Optional[str] = None
        self.mobile: Optional[str] = None
        self.email: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "UserContactInfoBuilder":
        return UserContactInfoBuilder()


class UserContactInfoBuilder(object):
    def __init__(self) -> None:
        self._user_contact_info = UserContactInfo()

    def user_id(self, user_id: str) -> "UserContactInfoBuilder":
        self._user_contact_info.user_id = user_id
        return self

    def mobile(self, mobile: str) -> "UserContactInfoBuilder":
        self._user_contact_info.mobile = mobile
        return self

    def email(self, email: str) -> "UserContactInfoBuilder":
        self._user_contact_info.email = email
        return self

    def build(self) -> "UserContactInfo":
        return self._user_contact_info
