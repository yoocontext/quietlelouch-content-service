from dataclasses import dataclass
from enum import Enum

from .base import BaseEntity


@dataclass(kw_only=True)
class Manga(BaseEntity):
    title: str
    media_type: "MediaType"
    pages_count: int
    pages: list["Page"]
    tags: list["Tag"]


@dataclass(kw_only=True)
class Image(BaseEntity):
    title: str
    url: str
    height: int
    weight: int
    size: int
    media_type: "MediaType"


@dataclass(kw_only=True)
class Gif(BaseEntity):
    title: str
    url: str
    height: int
    weight: int
    size: int
    duration: int
    media_type: "MediaType"


@dataclass(kw_only=True)
class Video(BaseEntity):
    title: str
    url: str
    height: int
    weight: int
    size: int
    duration: int
    media_type: "MediaType"


@dataclass(kw_only=True)
class Page(BaseEntity):
    url: str
    height: int
    weight: int
    size: int


class MediaType(Enum):
    JPEG = "image/jpeg"
    PNG = "image/png"
    GIF = "image/gif"
    MP4 = "video/mp4"


class Tag(BaseEntity):
    name: str
    description: str | None = None
