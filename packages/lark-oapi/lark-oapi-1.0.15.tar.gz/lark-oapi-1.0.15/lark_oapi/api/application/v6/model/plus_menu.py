# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class PlusMenu(object):
    _types = {
        "pc_app_link": str,
        "mobile_app_link": str,
    }

    def __init__(self, d=None):
        self.pc_app_link: Optional[str] = None
        self.mobile_app_link: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "PlusMenuBuilder":
        return PlusMenuBuilder()


class PlusMenuBuilder(object):
    def __init__(self) -> None:
        self._plus_menu = PlusMenu()

    def pc_app_link(self, pc_app_link: str) -> "PlusMenuBuilder":
        self._plus_menu.pc_app_link = pc_app_link
        return self

    def mobile_app_link(self, mobile_app_link: str) -> "PlusMenuBuilder":
        self._plus_menu.mobile_app_link = mobile_app_link
        return self

    def build(self) -> "PlusMenu":
        return self._plus_menu
