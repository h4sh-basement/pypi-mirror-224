# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .content_text_style import ContentTextStyle


class ContentTextRun(object):
    _types = {
        "text": str,
        "style": ContentTextStyle,
    }

    def __init__(self, d=None):
        self.text: Optional[str] = None
        self.style: Optional[ContentTextStyle] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ContentTextRunBuilder":
        return ContentTextRunBuilder()


class ContentTextRunBuilder(object):
    def __init__(self) -> None:
        self._content_text_run = ContentTextRun()

    def text(self, text: str) -> "ContentTextRunBuilder":
        self._content_text_run.text = text
        return self

    def style(self, style: ContentTextStyle) -> "ContentTextRunBuilder":
        self._content_text_run.style = style
        return self

    def build(self) -> "ContentTextRun":
        return self._content_text_run
