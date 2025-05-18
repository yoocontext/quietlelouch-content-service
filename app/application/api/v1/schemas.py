from typing import Optional

from pydantic import BaseModel


class TagCreateSchema(BaseModel):
    name: str
    description: Optional[str]


class RoleCreateSchema(BaseModel):
    name: str
    description: Optional[str]


class TitleCreateSchema(BaseModel):
    name: str


class AuthorCreateSchema(BaseModel):
    name: str
    bio: Optional[str]


class LanguageCreateSchema(BaseModel):
    name: str
    description: Optional[str]
