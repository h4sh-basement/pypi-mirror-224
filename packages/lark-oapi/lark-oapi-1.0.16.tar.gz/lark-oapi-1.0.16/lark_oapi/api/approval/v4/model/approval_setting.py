# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class ApprovalSetting(object):
    _types = {
        "revert_interval": int,
        "revert_option": int,
        "reject_option": int,
        "quick_approval_option": int,
    }

    def __init__(self, d=None):
        self.revert_interval: Optional[int] = None
        self.revert_option: Optional[int] = None
        self.reject_option: Optional[int] = None
        self.quick_approval_option: Optional[int] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ApprovalSettingBuilder":
        return ApprovalSettingBuilder()


class ApprovalSettingBuilder(object):
    def __init__(self) -> None:
        self._approval_setting = ApprovalSetting()

    def revert_interval(self, revert_interval: int) -> "ApprovalSettingBuilder":
        self._approval_setting.revert_interval = revert_interval
        return self

    def revert_option(self, revert_option: int) -> "ApprovalSettingBuilder":
        self._approval_setting.revert_option = revert_option
        return self

    def reject_option(self, reject_option: int) -> "ApprovalSettingBuilder":
        self._approval_setting.reject_option = reject_option
        return self

    def quick_approval_option(self, quick_approval_option: int) -> "ApprovalSettingBuilder":
        self._approval_setting.quick_approval_option = quick_approval_option
        return self

    def build(self) -> "ApprovalSetting":
        return self._approval_setting
