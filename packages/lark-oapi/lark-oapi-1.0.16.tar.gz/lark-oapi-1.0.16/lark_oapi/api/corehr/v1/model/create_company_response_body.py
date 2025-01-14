# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .company import Company


class CreateCompanyResponseBody(object):
    _types = {
        "company": Company,
    }

    def __init__(self, d=None):
        self.company: Optional[Company] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "CreateCompanyResponseBodyBuilder":
        return CreateCompanyResponseBodyBuilder()


class CreateCompanyResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._create_company_response_body = CreateCompanyResponseBody()

    def company(self, company: Company) -> "CreateCompanyResponseBodyBuilder":
        self._create_company_response_body.company = company
        return self

    def build(self) -> "CreateCompanyResponseBody":
        return self._create_company_response_body
