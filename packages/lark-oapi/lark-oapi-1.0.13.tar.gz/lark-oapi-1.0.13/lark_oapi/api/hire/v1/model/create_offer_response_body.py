# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .offer_basic_info import OfferBasicInfo
from .offer_customized_info import OfferCustomizedInfo
from .offer_salary_info import OfferSalaryInfo


class CreateOfferResponseBody(object):
    _types = {
        "offer_id": str,
        "application_id": str,
        "schema_id": str,
        "offer_type": int,
        "basic_info": OfferBasicInfo,
        "salary_info": OfferSalaryInfo,
        "customized_info_list": List[OfferCustomizedInfo],
    }

    def __init__(self, d=None):
        self.offer_id: Optional[str] = None
        self.application_id: Optional[str] = None
        self.schema_id: Optional[str] = None
        self.offer_type: Optional[int] = None
        self.basic_info: Optional[OfferBasicInfo] = None
        self.salary_info: Optional[OfferSalaryInfo] = None
        self.customized_info_list: Optional[List[OfferCustomizedInfo]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "CreateOfferResponseBodyBuilder":
        return CreateOfferResponseBodyBuilder()


class CreateOfferResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._create_offer_response_body = CreateOfferResponseBody()

    def offer_id(self, offer_id: str) -> "CreateOfferResponseBodyBuilder":
        self._create_offer_response_body.offer_id = offer_id
        return self

    def application_id(self, application_id: str) -> "CreateOfferResponseBodyBuilder":
        self._create_offer_response_body.application_id = application_id
        return self

    def schema_id(self, schema_id: str) -> "CreateOfferResponseBodyBuilder":
        self._create_offer_response_body.schema_id = schema_id
        return self

    def offer_type(self, offer_type: int) -> "CreateOfferResponseBodyBuilder":
        self._create_offer_response_body.offer_type = offer_type
        return self

    def basic_info(self, basic_info: OfferBasicInfo) -> "CreateOfferResponseBodyBuilder":
        self._create_offer_response_body.basic_info = basic_info
        return self

    def salary_info(self, salary_info: OfferSalaryInfo) -> "CreateOfferResponseBodyBuilder":
        self._create_offer_response_body.salary_info = salary_info
        return self

    def customized_info_list(self, customized_info_list: List[OfferCustomizedInfo]) -> "CreateOfferResponseBodyBuilder":
        self._create_offer_response_body.customized_info_list = customized_info_list
        return self

    def build(self) -> "CreateOfferResponseBody":
        return self._create_offer_response_body
