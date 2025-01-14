# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .link import Link


class TextElementStyle(object):
    _types = {
        "bold": bool,
        "italic": bool,
        "strikethrough": bool,
        "underline": bool,
        "inline_code": bool,
        "background_color": int,
        "text_color": int,
        "link": Link,
        "comment_ids": List[str],
    }

    def __init__(self, d=None):
        self.bold: Optional[bool] = None
        self.italic: Optional[bool] = None
        self.strikethrough: Optional[bool] = None
        self.underline: Optional[bool] = None
        self.inline_code: Optional[bool] = None
        self.background_color: Optional[int] = None
        self.text_color: Optional[int] = None
        self.link: Optional[Link] = None
        self.comment_ids: Optional[List[str]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "TextElementStyleBuilder":
        return TextElementStyleBuilder()


class TextElementStyleBuilder(object):
    def __init__(self) -> None:
        self._text_element_style = TextElementStyle()

    def bold(self, bold: bool) -> "TextElementStyleBuilder":
        self._text_element_style.bold = bold
        return self

    def italic(self, italic: bool) -> "TextElementStyleBuilder":
        self._text_element_style.italic = italic
        return self

    def strikethrough(self, strikethrough: bool) -> "TextElementStyleBuilder":
        self._text_element_style.strikethrough = strikethrough
        return self

    def underline(self, underline: bool) -> "TextElementStyleBuilder":
        self._text_element_style.underline = underline
        return self

    def inline_code(self, inline_code: bool) -> "TextElementStyleBuilder":
        self._text_element_style.inline_code = inline_code
        return self

    def background_color(self, background_color: int) -> "TextElementStyleBuilder":
        self._text_element_style.background_color = background_color
        return self

    def text_color(self, text_color: int) -> "TextElementStyleBuilder":
        self._text_element_style.text_color = text_color
        return self

    def link(self, link: Link) -> "TextElementStyleBuilder":
        self._text_element_style.link = link
        return self

    def comment_ids(self, comment_ids: List[str]) -> "TextElementStyleBuilder":
        self._text_element_style.comment_ids = comment_ids
        return self

    def build(self) -> "TextElementStyle":
        return self._text_element_style
