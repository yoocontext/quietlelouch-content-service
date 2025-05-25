from dataclasses import dataclass, field
from typing import Annotated, Optional
from uuid import UUID

from domain.entities.content import Image
from domain.logic.use_cases import (
    BaseUseCase,
    BaseCommand,
    BaseResult,
)
from infra.pg.dao.image import ImageDao
from infra.pg.dto.image import ImageUpdateDto
from infra.pg.models import ImageOrm
from infra.pg.repository import ImageRepository
from infra.s3.boto_client import BotoClient
from infra.s3.const import ClientMethod, Bucket


@dataclass
class UpdateImageCommand(BaseCommand):
    image_uid: UUID
    tags: Optional["UpdateTags"] = None
    access_roles: Optional["UpdateAccessRoles"] = None
    name: str | None = None
    description: str | None = None
    nsfw: bool | None = None
    title: str | None = None
    author: Annotated[str | None, "author name"] = None
    language: Annotated[str | None, "language name"] = None

    fields_set: set[str] = field(default_factory=set)

    @dataclass
    class UpdateTags:
        to_add: Annotated[set[str], "tag names"] = field(default_factory=set)
        to_remove: Annotated[set[str], "tag names"] = field(default_factory=set)

    @dataclass
    class UpdateAccessRoles:
        to_add: Annotated[set[str], "role names"] = field(default_factory=set)
        to_remove: Annotated[set[str], "role names"] = field(default_factory=set)


@dataclass(kw_only=True)
class UpdateImageResult(BaseResult):
    uid: UUID
    url: str
    name: str
    description: str | None = None
    nsfw: bool | None = None
    tags: Annotated[set[str], "tag names"] = field(default_factory=set)
    title: str | None = None
    author: Annotated[str | None, "author name"] = None
    language: Annotated[str | None, "language name"] = None
    width: int
    height: int
    size: int
    content_type: str


@dataclass
class UpdateImageUseCase(BaseUseCase):
    image_repository: ImageRepository
    image_dao: ImageDao
    s3_client: BotoClient

    async def act(self, command: UpdateImageCommand) -> UpdateImageResult:
        image_orm: ImageOrm = await self.image_dao.get(uid=command.image_uid)

        update_tags: set[str] = {tag.name for tag in image_orm.tags}
        update_access_roles: set[str] = {access_role.name for access_role in image_orm.access_roles}

        if command.tags:
            update_tags: set[str] = (update_tags | command.tags.to_add) - command.tags.to_remove

        if command.access_roles:
            update_access_roles: set[str] = (
                    (update_access_roles | command.access_roles.to_add) - command.access_roles.to_remove
                )

        image_update = ImageUpdateDto(
            tags=update_tags,
            access_roles=update_access_roles,
            uid=command.image_uid,
            name=command.name,
            description=command.description,
            nsfw=command.nsfw,
            title=command.title,
            author=command.author,
            language=command.language,
            fields_set=command.fields_set,
        )
        image: Image = await self.image_repository.update(update_dto=image_update)
        description: str | None = image.description.as_generic_type() if image.description else None
        title: str | None = image.title.as_generic_type() if image.title else None

        await self.image_repository.session.refresh(image_orm)
        author: str | None = image_orm.author.name if image_orm.author else None
        language: str | None = image_orm.language.name if image_orm.language else None


        url: str = await self.s3_client.generate_presigned_url(
            client_method=ClientMethod.GET_OBJECT.value,
            params={
                'Bucket': Bucket.IMAGE.value,
                'Key': str(image.uid),
            },
            http_method='GET'
        )

        result = UpdateImageResult(
            uid=image.uid,
            url=url,
            name=image.name.as_generic_type(),
            description=description,
            nsfw=image_orm.nsfw,
            tags=update_tags,
            title=title,
            author=author,
            language=language,
            width=image.width,
            height=image.height,
            size=image.size.as_generic_type(),
            content_type=image.media_type.value,
        )

        await self.image_repository.session.commit()

        return result


