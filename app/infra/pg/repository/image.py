from dataclasses import dataclass
from uuid import UUID

from domain.entities.content import Image
from infra.pg.dao.image import ImageDao
from infra.pg.models import TagOrm, RoleOrm, TitleOrm, AuthorOrm, LanguageOrm
from infra.pg.models.content import (
    ImageOrm,
)
from infra.pg.dao.author import AuthorDao
from infra.pg.dao.language import LanguageDao
from infra.pg.dao.role import RoleDao
from infra.pg.dao.tag import TagDao
from infra.pg.dao.title import TitleDao
from infra.pg.dto.image import ImageCreateDto, ImageUpdateDto
from infra.pg.repository.base import BaseRepository
from infra.pg.mappers import (
    ImageOrmToEntityMapper,
)
from infra.pg.schemas.image import ImageUpdateSchema
from infra.pg.utils import update_orm


@dataclass
class ImageRepository(BaseRepository):
    image_dao: ImageDao
    tag_dao: TagDao
    role_dao: RoleDao
    title_dao: TitleDao
    author_dao: AuthorDao
    language_dao: LanguageDao
    mapper: ImageOrmToEntityMapper

    async def get_by_uid(self, uid: UUID) -> Image:
        image_orm: ImageOrm = await self.image_dao.get(uid=uid)
        image: Image = self.mapper.get_image(image_orm)

        return image

    async def create(self, create_schema: ImageCreateDto) -> Image:
        tags_orm: list[TagOrm] = await self.tag_dao.get_by_names(names=create_schema.tags)
        access_roles_orm: list[RoleOrm] = await self.role_dao.get_by_names(names=create_schema.access_roles)

        title_orm: TitleOrm | None = None
        author_orm: AuthorOrm | None = None
        language_orm: LanguageOrm | None = None

        if create_schema.title:
            title_orm: TitleOrm = await self.title_dao.get_by_name(name=create_schema.title)
        if create_schema.author:
            author_orm: AuthorOrm = await self.author_dao.get_by_name(name=create_schema.author)
        if create_schema.language:
            language_orm: LanguageOrm = await self.language_dao.get_by_name(name=create_schema.language)

        image_orm = ImageOrm(
            uid=create_schema.uid,
            name=create_schema.name,
            description=create_schema.description,
            height=create_schema.height,
            width=create_schema.width,
            size=create_schema.size,
            media_type=create_schema.media_type,
            nsfw=create_schema.nsfw,
            added_by=create_schema.added_by,
            tags=tags_orm,
            access_roles=access_roles_orm,
            title=title_orm,
            author=author_orm,
            language=language_orm,
        )

        self.session.add(image_orm)
        await self.session.flush()
        await self.session.refresh(image_orm)

        image: Image = self.mapper.get_image(image_orm)

        return image

    async def delete(self, uid: UUID) -> None:
        await self.image_dao.delete(uid=uid)

    async def update(self, update_dto: ImageUpdateDto) -> Image:
        tags_orm: list[TagOrm] = []
        access_roles_orm: list[RoleOrm] = []
        title_orm: TitleOrm | None = None
        author_orm: AuthorOrm | None = None
        language_orm: LanguageOrm | None = None

        if update_dto.tags:
            tags_orm: list[TagOrm] = await self.tag_dao.get_by_names(names=update_dto.tags)
        if update_dto.access_roles:
            access_roles_orm: list[RoleOrm] = await self.role_dao.get_by_names(names=update_dto.access_roles)
        if update_dto.title:
            title_orm: TitleOrm = await self.title_dao.get_by_name(name=update_dto.title)
        if update_dto.author:
            author_orm: AuthorOrm = await self.author_dao.get_by_name(name=update_dto.author)
        if update_dto.language:
            language_orm: LanguageOrm = await self.language_dao.get_by_name(name=update_dto.language)

        image_orm: ImageOrm = await self.image_dao.get(uid=update_dto.uid)

        update_schema = ImageUpdateSchema(
            _fields_set=update_dto.fields_set,
            name=update_dto.name,
            description=update_dto.description,
            nsfw=update_dto.nsfw,
            tags=tags_orm,
            access_roles=access_roles_orm,
            title=title_orm,
            author=author_orm,
            language=language_orm,
        )
        image_orm: ImageOrm = update_orm(schema=update_schema, orm=image_orm)
        image: Image = self.mapper.get_image(image_orm=image_orm)

        return image
