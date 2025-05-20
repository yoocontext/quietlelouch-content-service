from dataclasses import dataclass
from uuid import UUID

from domain.entities.content import Image
from infra.pg.models import TagOrm, RoleOrm, TitleOrm, AuthorOrm, LanguageOrm
from infra.pg.models.content import (
    ImageOrm,
)
from infra.pg.repository.author import AuthorRepository
from infra.pg.repository.common.base import BaseRepository
from infra.pg.repository.language import LanguageRepository
from infra.pg.repository.role import RoleRepository
from infra.pg.repository.tag import TagRepository
from infra.pg.repository.common.exceptions import ObjectNotFoundException
from infra.pg.repository.title import TitleRepository
from infra.pg.schemas.image import ImageCreateSchema
from infra.pg.mappers import (
    ContentOrmToEntityMapper,
    ContentCreateSchemaToOrmMapper
)


@dataclass
class ImageRepository(BaseRepository):
    tag_repository: TagRepository
    role_repository: RoleRepository
    title_repository: TitleRepository
    author_repository: AuthorRepository
    language_repository: LanguageRepository
    schema_mapper: ContentCreateSchemaToOrmMapper
    orm_mapper: ContentOrmToEntityMapper

    async def get_by_uid(self, uid: UUID) -> ImageOrm:
        image: ImageOrm | None = await self.session.get(ImageOrm, uid)
        if image:
            return image
        else:
            raise ObjectNotFoundException(required_obj=uid)


    async def create(self, image_schema: ImageCreateSchema) -> Image:
        tags_orm: list[TagOrm] = await self.tag_repository.get_by_names(names=image_schema.tags)
        access_roles_orm: list[RoleOrm] = await self.role_repository.get_by_names(names=image_schema.access_roles)
        language_orm: LanguageOrm = await self.language_repository.get_by_name(name=image_schema.language)

        title_orm: TitleOrm | None = None
        author_orm: AuthorOrm | None = None

        if image_schema.title:
            title_orm: TitleOrm = await self.title_repository.get_by_name(name=image_schema.title)
        if image_schema.author:
            author_orm: AuthorOrm = await self.author_repository.get_by_name(name=image_schema.author)

        image_orm = ImageOrm(
            name=image_schema.name,
            description=image_schema.description,
            height=image_schema.height,
            width=image_schema.width,
            size=image_schema.size,
            media_type=image_schema.media_type,
            nsfw=image_schema.nsfw,
            added_by=image_schema.added_by,
            tags=tags_orm,
            access_roles=access_roles_orm,
            title=title_orm,
            author=author_orm,
            language=language_orm,
        )

        self.session.add(image_orm)
        await self.session.flush()
        await self.session.refresh(image_orm)

        image: Image = self.orm_mapper.get_image(image_orm)

        return image
