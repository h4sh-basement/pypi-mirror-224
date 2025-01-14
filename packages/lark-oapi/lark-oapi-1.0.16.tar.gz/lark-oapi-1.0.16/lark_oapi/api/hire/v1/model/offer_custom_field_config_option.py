# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .i18n import I18n


class OfferCustomFieldConfigOption(object):
    _types = {
        "name": I18n,
    }

    def __init__(self, d=None):
        self.name: Optional[I18n] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "OfferCustomFieldConfigOptionBuilder":
        return OfferCustomFieldConfigOptionBuilder()


class OfferCustomFieldConfigOptionBuilder(object):
    def __init__(self) -> None:
        self._offer_custom_field_config_option = OfferCustomFieldConfigOption()

    def name(self, name: I18n) -> "OfferCustomFieldConfigOptionBuilder":
        self._offer_custom_field_config_option.name = name
        return self

    def build(self) -> "OfferCustomFieldConfigOption":
        return self._offer_custom_field_config_option
