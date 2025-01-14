# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .client_badge_num import ClientBadgeNum


class AppBadge(object):
    _types = {
        "user_id": int,
        "version": int,
        "extra": str,
        "pc": ClientBadgeNum,
        "mobile": ClientBadgeNum,
    }

    def __init__(self, d=None):
        self.user_id: Optional[int] = None
        self.version: Optional[int] = None
        self.extra: Optional[str] = None
        self.pc: Optional[ClientBadgeNum] = None
        self.mobile: Optional[ClientBadgeNum] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "AppBadgeBuilder":
        return AppBadgeBuilder()


class AppBadgeBuilder(object):
    def __init__(self) -> None:
        self._app_badge = AppBadge()

    def user_id(self, user_id: int) -> "AppBadgeBuilder":
        self._app_badge.user_id = user_id
        return self

    def version(self, version: int) -> "AppBadgeBuilder":
        self._app_badge.version = version
        return self

    def extra(self, extra: str) -> "AppBadgeBuilder":
        self._app_badge.extra = extra
        return self

    def pc(self, pc: ClientBadgeNum) -> "AppBadgeBuilder":
        self._app_badge.pc = pc
        return self

    def mobile(self, mobile: ClientBadgeNum) -> "AppBadgeBuilder":
        self._app_badge.mobile = mobile
        return self

    def build(self) -> "AppBadge":
        return self._app_badge
