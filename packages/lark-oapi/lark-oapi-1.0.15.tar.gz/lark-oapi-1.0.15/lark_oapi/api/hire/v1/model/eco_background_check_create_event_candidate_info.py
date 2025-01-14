# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .eco_background_check_create_event_mobile import EcoBackgroundCheckCreateEventMobile


class EcoBackgroundCheckCreateEventCandidateInfo(object):
    _types = {
        "name": str,
        "mobile": EcoBackgroundCheckCreateEventMobile,
        "email": str,
    }

    def __init__(self, d=None):
        self.name: Optional[str] = None
        self.mobile: Optional[EcoBackgroundCheckCreateEventMobile] = None
        self.email: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "EcoBackgroundCheckCreateEventCandidateInfoBuilder":
        return EcoBackgroundCheckCreateEventCandidateInfoBuilder()


class EcoBackgroundCheckCreateEventCandidateInfoBuilder(object):
    def __init__(self) -> None:
        self._eco_background_check_create_event_candidate_info = EcoBackgroundCheckCreateEventCandidateInfo()

    def name(self, name: str) -> "EcoBackgroundCheckCreateEventCandidateInfoBuilder":
        self._eco_background_check_create_event_candidate_info.name = name
        return self

    def mobile(self,
               mobile: EcoBackgroundCheckCreateEventMobile) -> "EcoBackgroundCheckCreateEventCandidateInfoBuilder":
        self._eco_background_check_create_event_candidate_info.mobile = mobile
        return self

    def email(self, email: str) -> "EcoBackgroundCheckCreateEventCandidateInfoBuilder":
        self._eco_background_check_create_event_candidate_info.email = email
        return self

    def build(self) -> "EcoBackgroundCheckCreateEventCandidateInfo":
        return self._eco_background_check_create_event_candidate_info
