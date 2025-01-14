# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .appli_talent_attach_resume_info import AppliTalentAttachResumeInfo
from .appli_talent_certificate_info import AppliTalentCertificateInfo
from .appli_talent_competition_info import AppliTalentCompetitionInfo
from .appli_talent_education_info import AppliTalentEducationInfo
from .application_talent_award_info import ApplicationTalentAwardInfo
from .application_talent_basic_info import ApplicationTalentBasicInfo
from .application_talent_career_info import ApplicationTalentCareerInfo
from .application_talent_language_info import ApplicationTalentLanguageInfo
from .application_talent_project_info import ApplicationTalentProjectInfo
from .application_talent_sns_info import ApplicationTalentSnsInfo
from .application_talent_works_info import ApplicationTalentWorksInfo


class ApplicationTalent(object):
    _types = {
        "id": str,
        "basic_info": ApplicationTalentBasicInfo,
        "self_evaluation": str,
        "education_list": List[AppliTalentEducationInfo],
        "career_list": List[ApplicationTalentCareerInfo],
        "project_list": List[ApplicationTalentProjectInfo],
        "works_list": List[ApplicationTalentWorksInfo],
        "award_list": List[ApplicationTalentAwardInfo],
        "competition_list": List[AppliTalentCompetitionInfo],
        "certificate_list": List[AppliTalentCertificateInfo],
        "language_list": List[ApplicationTalentLanguageInfo],
        "sns_list": List[ApplicationTalentSnsInfo],
        "attachment_resume_list": List[AppliTalentAttachResumeInfo],
    }

    def __init__(self, d=None):
        self.id: Optional[str] = None
        self.basic_info: Optional[ApplicationTalentBasicInfo] = None
        self.self_evaluation: Optional[str] = None
        self.education_list: Optional[List[AppliTalentEducationInfo]] = None
        self.career_list: Optional[List[ApplicationTalentCareerInfo]] = None
        self.project_list: Optional[List[ApplicationTalentProjectInfo]] = None
        self.works_list: Optional[List[ApplicationTalentWorksInfo]] = None
        self.award_list: Optional[List[ApplicationTalentAwardInfo]] = None
        self.competition_list: Optional[List[AppliTalentCompetitionInfo]] = None
        self.certificate_list: Optional[List[AppliTalentCertificateInfo]] = None
        self.language_list: Optional[List[ApplicationTalentLanguageInfo]] = None
        self.sns_list: Optional[List[ApplicationTalentSnsInfo]] = None
        self.attachment_resume_list: Optional[List[AppliTalentAttachResumeInfo]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ApplicationTalentBuilder":
        return ApplicationTalentBuilder()


class ApplicationTalentBuilder(object):
    def __init__(self) -> None:
        self._application_talent = ApplicationTalent()

    def id(self, id: str) -> "ApplicationTalentBuilder":
        self._application_talent.id = id
        return self

    def basic_info(self, basic_info: ApplicationTalentBasicInfo) -> "ApplicationTalentBuilder":
        self._application_talent.basic_info = basic_info
        return self

    def self_evaluation(self, self_evaluation: str) -> "ApplicationTalentBuilder":
        self._application_talent.self_evaluation = self_evaluation
        return self

    def education_list(self, education_list: List[AppliTalentEducationInfo]) -> "ApplicationTalentBuilder":
        self._application_talent.education_list = education_list
        return self

    def career_list(self, career_list: List[ApplicationTalentCareerInfo]) -> "ApplicationTalentBuilder":
        self._application_talent.career_list = career_list
        return self

    def project_list(self, project_list: List[ApplicationTalentProjectInfo]) -> "ApplicationTalentBuilder":
        self._application_talent.project_list = project_list
        return self

    def works_list(self, works_list: List[ApplicationTalentWorksInfo]) -> "ApplicationTalentBuilder":
        self._application_talent.works_list = works_list
        return self

    def award_list(self, award_list: List[ApplicationTalentAwardInfo]) -> "ApplicationTalentBuilder":
        self._application_talent.award_list = award_list
        return self

    def competition_list(self, competition_list: List[AppliTalentCompetitionInfo]) -> "ApplicationTalentBuilder":
        self._application_talent.competition_list = competition_list
        return self

    def certificate_list(self, certificate_list: List[AppliTalentCertificateInfo]) -> "ApplicationTalentBuilder":
        self._application_talent.certificate_list = certificate_list
        return self

    def language_list(self, language_list: List[ApplicationTalentLanguageInfo]) -> "ApplicationTalentBuilder":
        self._application_talent.language_list = language_list
        return self

    def sns_list(self, sns_list: List[ApplicationTalentSnsInfo]) -> "ApplicationTalentBuilder":
        self._application_talent.sns_list = sns_list
        return self

    def attachment_resume_list(self,
                               attachment_resume_list: List[AppliTalentAttachResumeInfo]) -> "ApplicationTalentBuilder":
        self._application_talent.attachment_resume_list = attachment_resume_list
        return self

    def build(self) -> "ApplicationTalent":
        return self._application_talent
