from typing import Annotated

from pydantic import BaseModel, Field


class CreateImageInSchema(BaseModel):
    name: str
    description: str | None = None
    nsfw: bool
    tags: Annotated[set[str], "tag names"] = Field(default_factory=set)
    access_roles: Annotated[set[str], "role names"] = Field(default_factory=set)
    title: str | None = None
    author: Annotated[str | None, "author name"] = None
    language: Annotated[str | None, "language name"] = None


class CreateImageOutSchema(BaseModel):
    url: str
    width: int
    height: int
    size: int
    content_type: str


class GetImageOutSchema(BaseModel):
    url: str
    width: int
    height: int
    size: int
    content_type: str