from dataclasses import dataclass
from typing import Optional, Annotated
from uuid import UUID

from infra.pg.types import UserUid, SizeInBytes


@dataclass
class MangaCreateSchema:
    uid: Optional[UUID]
    name: str
    description: Optional[str]
    pages_count: int
    media_type: str
    nsfw: bool
    added_by: UserUid
    translated_by: Optional[UserUid]
    tags: Annotated[set[str], "tag names"]
    access_roles: Annotated[set[str], "role names"]
    pages: list["PageCreateSchema"]
    title: Optional["TitleCreateSchema"]
    author: Optional["AuthorCreateSchema"]
    language: "LanguageCreateSchema"


@dataclass
class PageCreateSchema:
    uid: Optional[UUID]
    height: int
    width: int
    size: SizeInBytes
    page_number: int


@dataclass
class TagCreateSchema:
    name: str
    description: Optional[str]


@dataclass
class RoleCreateSchema:
    name: str
    description: Optional[str]


@dataclass
class TitleCreateSchema:
    name: str


@dataclass
class AuthorCreateSchema:
    name: str
    bio: Optional[str]


@dataclass
class LanguageCreateSchema:
    name: str
    description: Optional[str]
