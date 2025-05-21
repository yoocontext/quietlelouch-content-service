from dataclasses import dataclass

from .base import BaseEntity
from domain.values.content import (
    NameValue,
    DescriptionValue,
    TitleValue,
    MediaTypeValue,
)


@dataclass(kw_only=True)
class Manga(BaseEntity):
    name: NameValue
    title: TitleValue | None
    description: DescriptionValue | None
    media_type: "MediaTypeValue"
    pages: list["Page"]
    tags: list["Tag"]


@dataclass(kw_only=True)
class Image(BaseEntity):
    name: NameValue
    title: TitleValue | None = None
    description: DescriptionValue | None = None
    media_type: "MediaTypeValue"


@dataclass(kw_only=True)
class Gif(BaseEntity):
    name: NameValue
    title: TitleValue | None
    description: DescriptionValue | None
    media_type: "MediaTypeValue"


@dataclass(kw_only=True)
class Video(BaseEntity):
    name: NameValue
    title: TitleValue | None
    description: DescriptionValue | None
    media_type: "MediaTypeValue"


@dataclass(kw_only=True)
class Page(BaseEntity):
    pass


@dataclass(kw_only=True)
class Tag(BaseEntity):
    name: NameValue
    description: DescriptionValue | None = None
