from uuid import UUID

from pydantic import BaseModel


class ImageCreateEvent(BaseModel):
    name: str
    description: str | None
    size: int
    media_type: str
    nsfw: bool
    added_by: UUID
    tags: set[str]
    access_roles: set[str]
    title: str | None
    language: str