from dataclasses import dataclass
from enum import Enum

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
    title: TitleValue | None
    description: DescriptionValue | None
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


class MediaType(Enum):
    JPEG = "image/jpeg"
    PNG = "image/png"
    GIF = "image/gif"
    MP4 = "video/mp4"


class Tag(BaseEntity):
    name: NameValue
    description: DescriptionValue | None = None
