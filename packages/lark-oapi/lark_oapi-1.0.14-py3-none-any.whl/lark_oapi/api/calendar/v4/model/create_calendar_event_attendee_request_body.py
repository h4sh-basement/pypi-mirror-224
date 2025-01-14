# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .calendar_event_attendee import CalendarEventAttendee


class CreateCalendarEventAttendeeRequestBody(object):
    _types = {
        "attendees": List[CalendarEventAttendee],
        "need_notification": bool,
        "instance_start_time_admin": str,
        "is_enable_admin": bool,
        "add_operator_to_attendee": bool,
    }

    def __init__(self, d=None):
        self.attendees: Optional[List[CalendarEventAttendee]] = None
        self.need_notification: Optional[bool] = None
        self.instance_start_time_admin: Optional[str] = None
        self.is_enable_admin: Optional[bool] = None
        self.add_operator_to_attendee: Optional[bool] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "CreateCalendarEventAttendeeRequestBodyBuilder":
        return CreateCalendarEventAttendeeRequestBodyBuilder()


class CreateCalendarEventAttendeeRequestBodyBuilder(object):
    def __init__(self) -> None:
        self._create_calendar_event_attendee_request_body = CreateCalendarEventAttendeeRequestBody()

    def attendees(self, attendees: List[CalendarEventAttendee]) -> "CreateCalendarEventAttendeeRequestBodyBuilder":
        self._create_calendar_event_attendee_request_body.attendees = attendees
        return self

    def need_notification(self, need_notification: bool) -> "CreateCalendarEventAttendeeRequestBodyBuilder":
        self._create_calendar_event_attendee_request_body.need_notification = need_notification
        return self

    def instance_start_time_admin(self,
                                  instance_start_time_admin: str) -> "CreateCalendarEventAttendeeRequestBodyBuilder":
        self._create_calendar_event_attendee_request_body.instance_start_time_admin = instance_start_time_admin
        return self

    def is_enable_admin(self, is_enable_admin: bool) -> "CreateCalendarEventAttendeeRequestBodyBuilder":
        self._create_calendar_event_attendee_request_body.is_enable_admin = is_enable_admin
        return self

    def add_operator_to_attendee(self,
                                 add_operator_to_attendee: bool) -> "CreateCalendarEventAttendeeRequestBodyBuilder":
        self._create_calendar_event_attendee_request_body.add_operator_to_attendee = add_operator_to_attendee
        return self

    def build(self) -> "CreateCalendarEventAttendeeRequestBody":
        return self._create_calendar_event_attendee_request_body
