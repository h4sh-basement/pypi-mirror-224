# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class Feature(object):
    _types = {
        "card": int,
        "face_uploaded": bool,
    }

    def __init__(self, d=None):
        self.card: Optional[int] = None
        self.face_uploaded: Optional[bool] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "FeatureBuilder":
        return FeatureBuilder()


class FeatureBuilder(object):
    def __init__(self) -> None:
        self._feature = Feature()

    def card(self, card: int) -> "FeatureBuilder":
        self._feature.card = card
        return self

    def face_uploaded(self, face_uploaded: bool) -> "FeatureBuilder":
        self._feature.face_uploaded = face_uploaded
        return self

    def build(self) -> "Feature":
        return self._feature
