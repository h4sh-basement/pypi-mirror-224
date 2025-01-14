# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .app_visibility import AppVisibility


class AppVersionRemark(object):
    _types = {
        "remark": str,
        "update_remark": str,
        "visibility": AppVisibility,
    }

    def __init__(self, d=None):
        self.remark: Optional[str] = None
        self.update_remark: Optional[str] = None
        self.visibility: Optional[AppVisibility] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "AppVersionRemarkBuilder":
        return AppVersionRemarkBuilder()


class AppVersionRemarkBuilder(object):
    def __init__(self) -> None:
        self._app_version_remark = AppVersionRemark()

    def remark(self, remark: str) -> "AppVersionRemarkBuilder":
        self._app_version_remark.remark = remark
        return self

    def update_remark(self, update_remark: str) -> "AppVersionRemarkBuilder":
        self._app_version_remark.update_remark = update_remark
        return self

    def visibility(self, visibility: AppVisibility) -> "AppVersionRemarkBuilder":
        self._app_version_remark.visibility = visibility
        return self

    def build(self) -> "AppVersionRemark":
        return self._app_version_remark
