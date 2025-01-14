# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .talent_customized_data_child import TalentCustomizedDataChild


class TalentLanguageInfo(object):
    _types = {
        "id": str,
        "language": int,
        "proficiency": int,
        "customized_data_list": List[TalentCustomizedDataChild],
    }

    def __init__(self, d=None):
        self.id: Optional[str] = None
        self.language: Optional[int] = None
        self.proficiency: Optional[int] = None
        self.customized_data_list: Optional[List[TalentCustomizedDataChild]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "TalentLanguageInfoBuilder":
        return TalentLanguageInfoBuilder()


class TalentLanguageInfoBuilder(object):
    def __init__(self) -> None:
        self._talent_language_info = TalentLanguageInfo()

    def id(self, id: str) -> "TalentLanguageInfoBuilder":
        self._talent_language_info.id = id
        return self

    def language(self, language: int) -> "TalentLanguageInfoBuilder":
        self._talent_language_info.language = language
        return self

    def proficiency(self, proficiency: int) -> "TalentLanguageInfoBuilder":
        self._talent_language_info.proficiency = proficiency
        return self

    def customized_data_list(self,
                             customized_data_list: List[TalentCustomizedDataChild]) -> "TalentLanguageInfoBuilder":
        self._talent_language_info.customized_data_list = customized_data_list
        return self

    def build(self) -> "TalentLanguageInfo":
        return self._talent_language_info
