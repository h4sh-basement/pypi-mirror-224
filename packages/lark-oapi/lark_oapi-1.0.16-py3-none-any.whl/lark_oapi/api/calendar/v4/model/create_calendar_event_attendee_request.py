# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest
from .create_calendar_event_attendee_request_body import CreateCalendarEventAttendeeRequestBody


class CreateCalendarEventAttendeeRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.user_id_type: Optional[str] = None
        self.calendar_id: Optional[str] = None
        self.event_id: Optional[str] = None
        self.request_body: Optional[CreateCalendarEventAttendeeRequestBody] = None

    @staticmethod
    def builder() -> "CreateCalendarEventAttendeeRequestBuilder":
        return CreateCalendarEventAttendeeRequestBuilder()


class CreateCalendarEventAttendeeRequestBuilder(object):

    def __init__(self) -> None:
        create_calendar_event_attendee_request = CreateCalendarEventAttendeeRequest()
        create_calendar_event_attendee_request.http_method = HttpMethod.POST
        create_calendar_event_attendee_request.uri = "/open-apis/calendar/v4/calendars/:calendar_id/events/:event_id/attendees"
        create_calendar_event_attendee_request.token_types = {AccessTokenType.TENANT, AccessTokenType.USER}
        self._create_calendar_event_attendee_request: CreateCalendarEventAttendeeRequest = create_calendar_event_attendee_request

    def user_id_type(self, user_id_type: str) -> "CreateCalendarEventAttendeeRequestBuilder":
        self._create_calendar_event_attendee_request.user_id_type = user_id_type
        self._create_calendar_event_attendee_request.add_query("user_id_type", user_id_type)
        return self

    def calendar_id(self, calendar_id: str) -> "CreateCalendarEventAttendeeRequestBuilder":
        self._create_calendar_event_attendee_request.calendar_id = calendar_id
        self._create_calendar_event_attendee_request.paths["calendar_id"] = str(calendar_id)
        return self

    def event_id(self, event_id: str) -> "CreateCalendarEventAttendeeRequestBuilder":
        self._create_calendar_event_attendee_request.event_id = event_id
        self._create_calendar_event_attendee_request.paths["event_id"] = str(event_id)
        return self

    def request_body(self,
                     request_body: CreateCalendarEventAttendeeRequestBody) -> "CreateCalendarEventAttendeeRequestBuilder":
        self._create_calendar_event_attendee_request.request_body = request_body
        self._create_calendar_event_attendee_request.body = request_body
        return self

    def build(self) -> CreateCalendarEventAttendeeRequest:
        return self._create_calendar_event_attendee_request
