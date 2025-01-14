# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class OffboardingChecklist(object):
    _types = {
        "checklist_status": str,
        "checklist_start_time": str,
        "checklist_finish_time": str,
        "checklist_process_id": str,
    }

    def __init__(self, d=None):
        self.checklist_status: Optional[str] = None
        self.checklist_start_time: Optional[str] = None
        self.checklist_finish_time: Optional[str] = None
        self.checklist_process_id: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "OffboardingChecklistBuilder":
        return OffboardingChecklistBuilder()


class OffboardingChecklistBuilder(object):
    def __init__(self) -> None:
        self._offboarding_checklist = OffboardingChecklist()

    def checklist_status(self, checklist_status: str) -> "OffboardingChecklistBuilder":
        self._offboarding_checklist.checklist_status = checklist_status
        return self

    def checklist_start_time(self, checklist_start_time: str) -> "OffboardingChecklistBuilder":
        self._offboarding_checklist.checklist_start_time = checklist_start_time
        return self

    def checklist_finish_time(self, checklist_finish_time: str) -> "OffboardingChecklistBuilder":
        self._offboarding_checklist.checklist_finish_time = checklist_finish_time
        return self

    def checklist_process_id(self, checklist_process_id: str) -> "OffboardingChecklistBuilder":
        self._offboarding_checklist.checklist_process_id = checklist_process_id
        return self

    def build(self) -> "OffboardingChecklist":
        return self._offboarding_checklist
