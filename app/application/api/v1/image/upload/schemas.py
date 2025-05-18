from typing import Annotated

from pydantic import BaseModel


class ImageCreateInSchema(BaseModel):
    name: str
    description: str | None
    nsfw: bool
    tags: Annotated[set[str], "tag names"]
    access_roles: Annotated[set[str], "role names"]
    title: str | None
    author: Annotated[str | None, "author name"]
    language: Annotated[str | None, "language name"]


class ImageCreateOutSchema(BaseModel):
    url: str
    width: int
    height: int
    size: int
    content_type: str
