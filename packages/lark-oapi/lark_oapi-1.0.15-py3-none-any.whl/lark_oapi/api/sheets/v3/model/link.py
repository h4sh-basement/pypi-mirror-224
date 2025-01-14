# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .segment_style import SegmentStyle


class Link(object):
    _types = {
        "text": str,
        "link": str,
        "segment_styles": List[SegmentStyle],
    }

    def __init__(self, d=None):
        self.text: Optional[str] = None
        self.link: Optional[str] = None
        self.segment_styles: Optional[List[SegmentStyle]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "LinkBuilder":
        return LinkBuilder()


class LinkBuilder(object):
    def __init__(self) -> None:
        self._link = Link()

    def text(self, text: str) -> "LinkBuilder":
        self._link.text = text
        return self

    def link(self, link: str) -> "LinkBuilder":
        self._link.link = link
        return self

    def segment_styles(self, segment_styles: List[SegmentStyle]) -> "LinkBuilder":
        self._link.segment_styles = segment_styles
        return self

    def build(self) -> "Link":
        return self._link
