# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .offer_apply_form_module_info import OfferApplyFormModuleInfo


class OfferApplyFormSchema(object):
    _types = {
        "id": str,
        "module_list": List[OfferApplyFormModuleInfo],
    }

    def __init__(self, d=None):
        self.id: Optional[str] = None
        self.module_list: Optional[List[OfferApplyFormModuleInfo]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "OfferApplyFormSchemaBuilder":
        return OfferApplyFormSchemaBuilder()


class OfferApplyFormSchemaBuilder(object):
    def __init__(self) -> None:
        self._offer_apply_form_schema = OfferApplyFormSchema()

    def id(self, id: str) -> "OfferApplyFormSchemaBuilder":
        self._offer_apply_form_schema.id = id
        return self

    def module_list(self, module_list: List[OfferApplyFormModuleInfo]) -> "OfferApplyFormSchemaBuilder":
        self._offer_apply_form_schema.module_list = module_list
        return self

    def build(self) -> "OfferApplyFormSchema":
        return self._offer_apply_form_schema
