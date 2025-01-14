# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class AppRecommendRuleVisibilityInfo(object):
    _types = {
        "is_all": bool,
        "department_ids": List[str],
        "user_ids": List[str],
        "group_ids": List[str],
    }

    def __init__(self, d=None):
        self.is_all: Optional[bool] = None
        self.department_ids: Optional[List[str]] = None
        self.user_ids: Optional[List[str]] = None
        self.group_ids: Optional[List[str]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "AppRecommendRuleVisibilityInfoBuilder":
        return AppRecommendRuleVisibilityInfoBuilder()


class AppRecommendRuleVisibilityInfoBuilder(object):
    def __init__(self) -> None:
        self._app_recommend_rule_visibility_info = AppRecommendRuleVisibilityInfo()

    def is_all(self, is_all: bool) -> "AppRecommendRuleVisibilityInfoBuilder":
        self._app_recommend_rule_visibility_info.is_all = is_all
        return self

    def department_ids(self, department_ids: List[str]) -> "AppRecommendRuleVisibilityInfoBuilder":
        self._app_recommend_rule_visibility_info.department_ids = department_ids
        return self

    def user_ids(self, user_ids: List[str]) -> "AppRecommendRuleVisibilityInfoBuilder":
        self._app_recommend_rule_visibility_info.user_ids = user_ids
        return self

    def group_ids(self, group_ids: List[str]) -> "AppRecommendRuleVisibilityInfoBuilder":
        self._app_recommend_rule_visibility_info.group_ids = group_ids
        return self

    def build(self) -> "AppRecommendRuleVisibilityInfo":
        return self._app_recommend_rule_visibility_info
