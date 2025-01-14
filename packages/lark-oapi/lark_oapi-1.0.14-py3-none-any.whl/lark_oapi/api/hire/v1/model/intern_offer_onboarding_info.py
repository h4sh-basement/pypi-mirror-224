# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class InternOfferOnboardingInfo(object):
    _types = {
        "actual_onboarding_date": str,
    }

    def __init__(self, d=None):
        self.actual_onboarding_date: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "InternOfferOnboardingInfoBuilder":
        return InternOfferOnboardingInfoBuilder()


class InternOfferOnboardingInfoBuilder(object):
    def __init__(self) -> None:
        self._intern_offer_onboarding_info = InternOfferOnboardingInfo()

    def actual_onboarding_date(self, actual_onboarding_date: str) -> "InternOfferOnboardingInfoBuilder":
        self._intern_offer_onboarding_info.actual_onboarding_date = actual_onboarding_date
        return self

    def build(self) -> "InternOfferOnboardingInfo":
        return self._intern_offer_onboarding_info
