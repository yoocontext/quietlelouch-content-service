from dataclasses import dataclass
from typing import Annotated
from uuid import UUID

from infra.pg.types import UserUid, SizeInBytes


@dataclass
class ImageCreateSchema:
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
