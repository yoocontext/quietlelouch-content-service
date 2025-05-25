from typing import Annotated
from uuid import UUID

from pydantic import BaseModel, Field


class CreateImageEvent(BaseModel):
    uid: UUID
    name: str
    description: str | None
    size: int
    media_type: str
    nsfw: bool
    added_by: UUID
    tags: set[str]
    access_roles: set[str]
    title: str | None
    language: str | None


class UpdateImageEvent(BaseModel):
    uid: UUID
    name: str | None
    description: str | None
    size: int | None
    media_type: str | None
    nsfw: bool | None
    tags: set[str]
    access_roles: set[str]
    title: str | None
    language: str | None


class DeleteImageEvent(BaseModel):
    uid: UUID