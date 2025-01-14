# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .ticket import Ticket
from .ticket_message_content import TicketMessageContent
from .user_id import UserId


class TicketMessageEvent(object):
    _types = {
        "ticket_message_id": str,
        "message_id": str,
        "msg_type": str,
        "position": str,
        "sender_id": UserId,
        "sender_type": int,
        "text": str,
        "ticket": Ticket,
        "event_id": str,
        "chat_id": str,
        "content": TicketMessageContent,
    }

    def __init__(self, d=None):
        self.ticket_message_id: Optional[str] = None
        self.message_id: Optional[str] = None
        self.msg_type: Optional[str] = None
        self.position: Optional[str] = None
        self.sender_id: Optional[UserId] = None
        self.sender_type: Optional[int] = None
        self.text: Optional[str] = None
        self.ticket: Optional[Ticket] = None
        self.event_id: Optional[str] = None
        self.chat_id: Optional[str] = None
        self.content: Optional[TicketMessageContent] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "TicketMessageEventBuilder":
        return TicketMessageEventBuilder()


class TicketMessageEventBuilder(object):
    def __init__(self) -> None:
        self._ticket_message_event = TicketMessageEvent()

    def ticket_message_id(self, ticket_message_id: str) -> "TicketMessageEventBuilder":
        self._ticket_message_event.ticket_message_id = ticket_message_id
        return self

    def message_id(self, message_id: str) -> "TicketMessageEventBuilder":
        self._ticket_message_event.message_id = message_id
        return self

    def msg_type(self, msg_type: str) -> "TicketMessageEventBuilder":
        self._ticket_message_event.msg_type = msg_type
        return self

    def position(self, position: str) -> "TicketMessageEventBuilder":
        self._ticket_message_event.position = position
        return self

    def sender_id(self, sender_id: UserId) -> "TicketMessageEventBuilder":
        self._ticket_message_event.sender_id = sender_id
        return self

    def sender_type(self, sender_type: int) -> "TicketMessageEventBuilder":
        self._ticket_message_event.sender_type = sender_type
        return self

    def text(self, text: str) -> "TicketMessageEventBuilder":
        self._ticket_message_event.text = text
        return self

    def ticket(self, ticket: Ticket) -> "TicketMessageEventBuilder":
        self._ticket_message_event.ticket = ticket
        return self

    def event_id(self, event_id: str) -> "TicketMessageEventBuilder":
        self._ticket_message_event.event_id = event_id
        return self

    def chat_id(self, chat_id: str) -> "TicketMessageEventBuilder":
        self._ticket_message_event.chat_id = chat_id
        return self

    def content(self, content: TicketMessageContent) -> "TicketMessageEventBuilder":
        self._ticket_message_event.content = content
        return self

    def build(self) -> "TicketMessageEvent":
        return self._ticket_message_event
