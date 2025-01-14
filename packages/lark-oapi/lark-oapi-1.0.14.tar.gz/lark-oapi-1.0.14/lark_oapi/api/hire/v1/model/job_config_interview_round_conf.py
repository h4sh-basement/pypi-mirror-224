# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class JobConfigInterviewRoundConf(object):
    _types = {
        "interviewer_id_list": List[str],
        "round": int,
    }

    def __init__(self, d=None):
        self.interviewer_id_list: Optional[List[str]] = None
        self.round: Optional[int] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "JobConfigInterviewRoundConfBuilder":
        return JobConfigInterviewRoundConfBuilder()


class JobConfigInterviewRoundConfBuilder(object):
    def __init__(self) -> None:
        self._job_config_interview_round_conf = JobConfigInterviewRoundConf()

    def interviewer_id_list(self, interviewer_id_list: List[str]) -> "JobConfigInterviewRoundConfBuilder":
        self._job_config_interview_round_conf.interviewer_id_list = interviewer_id_list
        return self

    def round(self, round: int) -> "JobConfigInterviewRoundConfBuilder":
        self._job_config_interview_round_conf.round = round
        return self

    def build(self) -> "JobConfigInterviewRoundConf":
        return self._job_config_interview_round_conf
