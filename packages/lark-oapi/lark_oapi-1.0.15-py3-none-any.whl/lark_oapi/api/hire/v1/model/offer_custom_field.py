# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .i18n import I18n
from .offer_custom_field_config import OfferCustomFieldConfig


class OfferCustomField(object):
    _types = {
        "id": str,
        "name": I18n,
        "config": OfferCustomFieldConfig,
    }

    def __init__(self, d=None):
        self.id: Optional[str] = None
        self.name: Optional[I18n] = None
        self.config: Optional[OfferCustomFieldConfig] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "OfferCustomFieldBuilder":
        return OfferCustomFieldBuilder()


class OfferCustomFieldBuilder(object):
    def __init__(self) -> None:
        self._offer_custom_field = OfferCustomField()

    def id(self, id: str) -> "OfferCustomFieldBuilder":
        self._offer_custom_field.id = id
        return self

    def name(self, name: I18n) -> "OfferCustomFieldBuilder":
        self._offer_custom_field.name = name
        return self

    def config(self, config: OfferCustomFieldConfig) -> "OfferCustomFieldBuilder":
        self._offer_custom_field.config = config
        return self

    def build(self) -> "OfferCustomField":
        return self._offer_custom_field
