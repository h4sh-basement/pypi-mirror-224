# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class UserReport2022(object):
    _types = {
        "user_id": str,
        "user_register_date": str,
        "active_day_count": int,
        "msg_busy_date": str,
        "msg_busy_date_send_msg_count": str,
        "p2p_chat_count": str,
        "talked_chat_count": str,
        "positive_reaction_count": str,
        "first_positive_reaction": str,
        "second_positive_reaction": str,
        "third_positive_reaction": str,
        "fourth_positive_reaction": str,
        "fifth_positive_reaction": str,
        "create_file_count": str,
        "created_file_view_count": str,
        "comment_file_count": str,
        "attend_event_count": str,
        "event_busy_date": str,
        "event_busy_date_event_count": str,
        "event_start_time_range1": str,
        "conference_create_count": str,
        "total_parti_count": str,
        "okr_cum_o_count": str,
        "okr_cum_kr_count": str,
        "okr_aligned_user_count": str,
        "people_interview_num": str,
        "send_email_count": str,
        "receive_email_count": str,
    }

    def __init__(self, d=None):
        self.user_id: Optional[str] = None
        self.user_register_date: Optional[str] = None
        self.active_day_count: Optional[int] = None
        self.msg_busy_date: Optional[str] = None
        self.msg_busy_date_send_msg_count: Optional[str] = None
        self.p2p_chat_count: Optional[str] = None
        self.talked_chat_count: Optional[str] = None
        self.positive_reaction_count: Optional[str] = None
        self.first_positive_reaction: Optional[str] = None
        self.second_positive_reaction: Optional[str] = None
        self.third_positive_reaction: Optional[str] = None
        self.fourth_positive_reaction: Optional[str] = None
        self.fifth_positive_reaction: Optional[str] = None
        self.create_file_count: Optional[str] = None
        self.created_file_view_count: Optional[str] = None
        self.comment_file_count: Optional[str] = None
        self.attend_event_count: Optional[str] = None
        self.event_busy_date: Optional[str] = None
        self.event_busy_date_event_count: Optional[str] = None
        self.event_start_time_range1: Optional[str] = None
        self.conference_create_count: Optional[str] = None
        self.total_parti_count: Optional[str] = None
        self.okr_cum_o_count: Optional[str] = None
        self.okr_cum_kr_count: Optional[str] = None
        self.okr_aligned_user_count: Optional[str] = None
        self.people_interview_num: Optional[str] = None
        self.send_email_count: Optional[str] = None
        self.receive_email_count: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "UserReport2022Builder":
        return UserReport2022Builder()


class UserReport2022Builder(object):
    def __init__(self) -> None:
        self._user_report2022 = UserReport2022()

    def user_id(self, user_id: str) -> "UserReport2022Builder":
        self._user_report2022.user_id = user_id
        return self

    def user_register_date(self, user_register_date: str) -> "UserReport2022Builder":
        self._user_report2022.user_register_date = user_register_date
        return self

    def active_day_count(self, active_day_count: int) -> "UserReport2022Builder":
        self._user_report2022.active_day_count = active_day_count
        return self

    def msg_busy_date(self, msg_busy_date: str) -> "UserReport2022Builder":
        self._user_report2022.msg_busy_date = msg_busy_date
        return self

    def msg_busy_date_send_msg_count(self, msg_busy_date_send_msg_count: str) -> "UserReport2022Builder":
        self._user_report2022.msg_busy_date_send_msg_count = msg_busy_date_send_msg_count
        return self

    def p2p_chat_count(self, p2p_chat_count: str) -> "UserReport2022Builder":
        self._user_report2022.p2p_chat_count = p2p_chat_count
        return self

    def talked_chat_count(self, talked_chat_count: str) -> "UserReport2022Builder":
        self._user_report2022.talked_chat_count = talked_chat_count
        return self

    def positive_reaction_count(self, positive_reaction_count: str) -> "UserReport2022Builder":
        self._user_report2022.positive_reaction_count = positive_reaction_count
        return self

    def first_positive_reaction(self, first_positive_reaction: str) -> "UserReport2022Builder":
        self._user_report2022.first_positive_reaction = first_positive_reaction
        return self

    def second_positive_reaction(self, second_positive_reaction: str) -> "UserReport2022Builder":
        self._user_report2022.second_positive_reaction = second_positive_reaction
        return self

    def third_positive_reaction(self, third_positive_reaction: str) -> "UserReport2022Builder":
        self._user_report2022.third_positive_reaction = third_positive_reaction
        return self

    def fourth_positive_reaction(self, fourth_positive_reaction: str) -> "UserReport2022Builder":
        self._user_report2022.fourth_positive_reaction = fourth_positive_reaction
        return self

    def fifth_positive_reaction(self, fifth_positive_reaction: str) -> "UserReport2022Builder":
        self._user_report2022.fifth_positive_reaction = fifth_positive_reaction
        return self

    def create_file_count(self, create_file_count: str) -> "UserReport2022Builder":
        self._user_report2022.create_file_count = create_file_count
        return self

    def created_file_view_count(self, created_file_view_count: str) -> "UserReport2022Builder":
        self._user_report2022.created_file_view_count = created_file_view_count
        return self

    def comment_file_count(self, comment_file_count: str) -> "UserReport2022Builder":
        self._user_report2022.comment_file_count = comment_file_count
        return self

    def attend_event_count(self, attend_event_count: str) -> "UserReport2022Builder":
        self._user_report2022.attend_event_count = attend_event_count
        return self

    def event_busy_date(self, event_busy_date: str) -> "UserReport2022Builder":
        self._user_report2022.event_busy_date = event_busy_date
        return self

    def event_busy_date_event_count(self, event_busy_date_event_count: str) -> "UserReport2022Builder":
        self._user_report2022.event_busy_date_event_count = event_busy_date_event_count
        return self

    def event_start_time_range1(self, event_start_time_range1: str) -> "UserReport2022Builder":
        self._user_report2022.event_start_time_range1 = event_start_time_range1
        return self

    def conference_create_count(self, conference_create_count: str) -> "UserReport2022Builder":
        self._user_report2022.conference_create_count = conference_create_count
        return self

    def total_parti_count(self, total_parti_count: str) -> "UserReport2022Builder":
        self._user_report2022.total_parti_count = total_parti_count
        return self

    def okr_cum_o_count(self, okr_cum_o_count: str) -> "UserReport2022Builder":
        self._user_report2022.okr_cum_o_count = okr_cum_o_count
        return self

    def okr_cum_kr_count(self, okr_cum_kr_count: str) -> "UserReport2022Builder":
        self._user_report2022.okr_cum_kr_count = okr_cum_kr_count
        return self

    def okr_aligned_user_count(self, okr_aligned_user_count: str) -> "UserReport2022Builder":
        self._user_report2022.okr_aligned_user_count = okr_aligned_user_count
        return self

    def people_interview_num(self, people_interview_num: str) -> "UserReport2022Builder":
        self._user_report2022.people_interview_num = people_interview_num
        return self

    def send_email_count(self, send_email_count: str) -> "UserReport2022Builder":
        self._user_report2022.send_email_count = send_email_count
        return self

    def receive_email_count(self, receive_email_count: str) -> "UserReport2022Builder":
        self._user_report2022.receive_email_count = receive_email_count
        return self

    def build(self) -> "UserReport2022":
        return self._user_report2022
