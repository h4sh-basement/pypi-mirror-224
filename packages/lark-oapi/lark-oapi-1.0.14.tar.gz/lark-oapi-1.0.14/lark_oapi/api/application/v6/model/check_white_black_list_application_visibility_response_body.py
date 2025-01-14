# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .application_visibility_department_white_black_info import ApplicationVisibilityDepartmentWhiteBlackInfo
from .application_visibility_group_white_black_info import ApplicationVisibilityGroupWhiteBlackInfo
from .application_visibility_user_white_black_info import ApplicationVisibilityUserWhiteBlackInfo


class CheckWhiteBlackListApplicationVisibilityResponseBody(object):
    _types = {
        "user_visibility_list": List[ApplicationVisibilityUserWhiteBlackInfo],
        "department_visibility_list": List[ApplicationVisibilityDepartmentWhiteBlackInfo],
        "group_visibility_list": List[ApplicationVisibilityGroupWhiteBlackInfo],
    }

    def __init__(self, d=None):
        self.user_visibility_list: Optional[List[ApplicationVisibilityUserWhiteBlackInfo]] = None
        self.department_visibility_list: Optional[List[ApplicationVisibilityDepartmentWhiteBlackInfo]] = None
        self.group_visibility_list: Optional[List[ApplicationVisibilityGroupWhiteBlackInfo]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "CheckWhiteBlackListApplicationVisibilityResponseBodyBuilder":
        return CheckWhiteBlackListApplicationVisibilityResponseBodyBuilder()


class CheckWhiteBlackListApplicationVisibilityResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._check_white_black_list_application_visibility_response_body = CheckWhiteBlackListApplicationVisibilityResponseBody()

    def user_visibility_list(self, user_visibility_list: List[
        ApplicationVisibilityUserWhiteBlackInfo]) -> "CheckWhiteBlackListApplicationVisibilityResponseBodyBuilder":
        self._check_white_black_list_application_visibility_response_body.user_visibility_list = user_visibility_list
        return self

    def department_visibility_list(self, department_visibility_list: List[
        ApplicationVisibilityDepartmentWhiteBlackInfo]) -> "CheckWhiteBlackListApplicationVisibilityResponseBodyBuilder":
        self._check_white_black_list_application_visibility_response_body.department_visibility_list = department_visibility_list
        return self

    def group_visibility_list(self, group_visibility_list: List[
        ApplicationVisibilityGroupWhiteBlackInfo]) -> "CheckWhiteBlackListApplicationVisibilityResponseBodyBuilder":
        self._check_white_black_list_application_visibility_response_body.group_visibility_list = group_visibility_list
        return self

    def build(self) -> "CheckWhiteBlackListApplicationVisibilityResponseBody":
        return self._check_white_black_list_application_visibility_response_body
