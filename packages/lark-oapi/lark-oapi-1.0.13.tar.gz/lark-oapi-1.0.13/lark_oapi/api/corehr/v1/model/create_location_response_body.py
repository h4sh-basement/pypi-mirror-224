# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .location import Location


class CreateLocationResponseBody(object):
    _types = {
        "location": Location,
    }

    def __init__(self, d=None):
        self.location: Optional[Location] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "CreateLocationResponseBodyBuilder":
        return CreateLocationResponseBodyBuilder()


class CreateLocationResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._create_location_response_body = CreateLocationResponseBody()

    def location(self, location: Location) -> "CreateLocationResponseBodyBuilder":
        self._create_location_response_body.location = location
        return self

    def build(self) -> "CreateLocationResponseBody":
        return self._create_location_response_body
