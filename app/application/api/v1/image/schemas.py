from typing import Annotated, Optional
from uuid import UUID

from pydantic import BaseModel, Field


class UploadImageInSchema(BaseModel):
    name: str
    description: str | None = None
    nsfw: bool
    tags: Annotated[set[str], "tag names"] = Field(default_factory=set)
    access_roles: Annotated[set[str], "role names"] = Field(default_factory=set)
    title: str | None = None
    author: Annotated[str | None, "author name"] = None
    language: Annotated[str | None, "language name"] = None


class CreateImageOutSchema(BaseModel):
    uid: UUID
    url: str
    name: str
    description: str | None = None
    nsfw: bool | None = None
    tags: Annotated[set[str], "tag names"] = Field(default_factory=set)
    title: str | None = None
    author: Annotated[str | None, "author name"] = None
    language: Annotated[str | None, "language name"] = None
    width: int
    height: int
    size: int
    content_type: str


class GetImageOutSchema(BaseModel):
    uid: UUID
    url: str
    name: str
    description: str | None = None
    nsfw: bool | None = None
    tags: Annotated[set[str], "tag names"] = Field(default_factory=set)
    title: str | None = None
    author: Annotated[str | None, "author name"] = None
    language: Annotated[str | None, "language name"] = None
    width: int
    height: int
    size: int
    content_type: str


class UpdateImageInSchema(BaseModel):
    name: str | None = None
    description: str | None = None
    nsfw: bool | None = None
    tags: Optional["UpdateTags"] = None
    access_roles: Optional["UpdateAccessRoles"] = None
    title: str | None = None
    author: Annotated[str | None, "author name"] = None
    language: Annotated[str | None, "language name"] = None

class UpdateTags(BaseModel):
    to_add: Annotated[set[str], "tag names"] = Field(default_factory=set)
    to_remove: Annotated[set[str], "tag names"] = Field(default_factory=set)

class UpdateAccessRoles(BaseModel):
    to_add: Annotated[set[str], "role names"] = Field(default_factory=set)
    to_remove: Annotated[set[str], "role names"] = Field(default_factory=set)


class UpdateImageOutSchema(BaseModel):
    uid: UUID
    url: str
    name: str
    description: str | None = None
    nsfw: bool | None = None
    tags: Annotated[set[str], "tag names"] = Field(default_factory=set)
    title: str | None = None
    author: Annotated[str | None, "author name"] = None
    language: Annotated[str | None, "language name"] = None
    width: int
    height: int
    size: int
    content_type: str