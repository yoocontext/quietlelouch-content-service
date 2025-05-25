from dataclasses import dataclass, field
from typing import Annotated, Optional
from uuid import UUID

from infra.pg.types import UserUid, SizeInBytes


@dataclass
class ImageCreateDto:
    uid: UUID | None
    name: str
    description: str | None
    height: int
    width: int
    size: SizeInBytes
    media_type: str
    nsfw: bool
    added_by: UserUid
    tags: Annotated[set[str], "tag names"]
    access_roles: Annotated[set[str], "role names"]
    title: str | None
    author: Annotated[str | None, "author name"]
    language: Annotated[str | None, "language name"]


@dataclass(kw_only=True)
class ImageUpdateDto:
    uid: UUID
    tags: Annotated[set[str], "tag names"] = field(default_factory=set)
    access_roles: Annotated[set[str], "role names"] = field(default_factory=set)
    name: str | None = None
    description: str | None = None
    nsfw: bool | None = None
    title: str | None = None
    author: Annotated[str | None, "author name"] = None
    language: Annotated[str | None, "language name"] = None

    fields_set: set[str]
