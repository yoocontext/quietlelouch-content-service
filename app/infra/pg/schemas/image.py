from dataclasses import dataclass

from .base import BaseUpdateInfraSchema
from infra.pg.models import AuthorOrm, LanguageOrm, TitleOrm, TagOrm, RoleOrm


@dataclass
class ImageUpdateSchema(BaseUpdateInfraSchema):
    tags: list[TagOrm] = None
    access_roles: list[RoleOrm] = None
    name: str | None = None
    description: str | None = None
    nsfw: bool | None = None
    title: TitleOrm = None
    author: AuthorOrm = None
    language: LanguageOrm = None