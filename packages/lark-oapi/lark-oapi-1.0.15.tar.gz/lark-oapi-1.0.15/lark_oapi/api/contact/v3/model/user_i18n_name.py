# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class UserI18nName(object):
    _types = {
        "zh_cn": str,
        "ja_jp": str,
        "en_us": str,
    }

    def __init__(self, d=None):
        self.zh_cn: Optional[str] = None
        self.ja_jp: Optional[str] = None
        self.en_us: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "UserI18nNameBuilder":
        return UserI18nNameBuilder()


class UserI18nNameBuilder(object):
    def __init__(self) -> None:
        self._user_i18n_name = UserI18nName()

    def zh_cn(self, zh_cn: str) -> "UserI18nNameBuilder":
        self._user_i18n_name.zh_cn = zh_cn
        return self

    def ja_jp(self, ja_jp: str) -> "UserI18nNameBuilder":
        self._user_i18n_name.ja_jp = ja_jp
        return self

    def en_us(self, en_us: str) -> "UserI18nNameBuilder":
        self._user_i18n_name.en_us = en_us
        return self

    def build(self) -> "UserI18nName":
        return self._user_i18n_name
