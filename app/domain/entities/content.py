from dataclasses import dataclass
from enum import Enum

from .base import BaseEntity


@dataclass(kw_only=True)
class Manga(BaseEntity):
    title: str
    extension: "Extension"
    pages_count: int
    pages: list["Page"]
    tags: list["Tag"]


@dataclass(kw_only=True)
class Image(BaseEntity):
    url: str
    height: int
    weight: int
    size: int
    extension: "Extension"


@dataclass(kw_only=True)
class Video(BaseEntity):
    url: str
    height: int
    weight: int
    size: int
    duration: int
    extension: "Extension"


@dataclass(kw_only=True)
class Gif(BaseEntity):
    url: str
    height: int
    weight: int
    size: int
    duration: int
    extension: "Extension"


@dataclass(kw_only=True)
class Page(BaseEntity):
    url: str
    height: int
    weight: int
    size: int


class Extension(Enum):
    jpeg: str = "jpeg"
    png: str = "png"
    git: str = "gif"
    mp4: str = "mp4"


class Tag(BaseEntity):
    name: str
    description: str | None = None
