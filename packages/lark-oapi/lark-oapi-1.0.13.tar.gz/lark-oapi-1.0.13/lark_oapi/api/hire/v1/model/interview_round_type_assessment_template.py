# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .i18n import I18n


class InterviewRoundTypeAssessmentTemplate(object):
    _types = {
        "id": str,
        "biz_id": str,
        "name": I18n,
    }

    def __init__(self, d=None):
        self.id: Optional[str] = None
        self.biz_id: Optional[str] = None
        self.name: Optional[I18n] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "InterviewRoundTypeAssessmentTemplateBuilder":
        return InterviewRoundTypeAssessmentTemplateBuilder()


class InterviewRoundTypeAssessmentTemplateBuilder(object):
    def __init__(self) -> None:
        self._interview_round_type_assessment_template = InterviewRoundTypeAssessmentTemplate()

    def id(self, id: str) -> "InterviewRoundTypeAssessmentTemplateBuilder":
        self._interview_round_type_assessment_template.id = id
        return self

    def biz_id(self, biz_id: str) -> "InterviewRoundTypeAssessmentTemplateBuilder":
        self._interview_round_type_assessment_template.biz_id = biz_id
        return self

    def name(self, name: I18n) -> "InterviewRoundTypeAssessmentTemplateBuilder":
        self._interview_round_type_assessment_template.name = name
        return self

    def build(self) -> "InterviewRoundTypeAssessmentTemplate":
        return self._interview_round_type_assessment_template
