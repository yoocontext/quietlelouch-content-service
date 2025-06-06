from dataclasses import dataclass
from typing import Annotated
from uuid import UUID

from fastapi import UploadFile # так делать прям оч точно нельзя, типа бизнес логика пиздец зависит от этой залупы
from faststream.rabbit import RabbitBroker

from domain.entities.content import Image
from domain.values.content.common import MediaType
from domain.logic.use_cases import BaseUseCase, BaseCommand, BaseResult
from domain.mappers.entities import ContentEntityMapper
from infra.pg.repository.image import ImageRepository
from infra.pg.dto.image import ImageCreateDto
from infra.rmq.events import CreateImageEvent
from infra.rmq.queues import CREATE_IMAGE
from infra.s3.boto_client import BotoClient
from infra.s3.const import Bucket, ClientMethod
from logic.services.meta.media_type import GetMediaTypeService
from logic.services.meta.metadata import GetPictureMetadataService, PictureMetadata


@dataclass
class UploadImageCommand(BaseCommand):
    file: UploadFile
    name: str
    description: str | None
    nsfw: bool
    user_uid: UUID
    tags: Annotated[set[str], "tag names"]
    access_roles: Annotated[set[str], "role names"]
    title: str | None
    author: Annotated[str | None, "author name"]
    language: Annotated[str | None, "language name"]


@dataclass(kw_only=True)
class UploadImageResult(BaseResult):
    uid: UUID
    url: str
    name: str
    description: str | None
    nsfw: bool | None = None
    tags: Annotated[set[str], "tag names"]
    title: str | None = None
    author: Annotated[str | None, "author name"]
    language: Annotated[str | None, "language name"]
    width: int
    height: int
    size: int
    content_type: str


@dataclass
class UploadImageUseCase(BaseUseCase):
    image_meta_service: GetPictureMetadataService
    get_media_type_service: GetMediaTypeService
    entity_mapper: ContentEntityMapper
    s3_client: BotoClient
    image_repository: ImageRepository
    broker: RabbitBroker

    async def act(self, command: UploadImageCommand) -> UploadImageResult:
        # todo проверить юзер роли

        image_metadata: PictureMetadata = await self.image_meta_service.act(file=command.file)
        media_type: MediaType = await self.get_media_type_service.act(format_type=image_metadata.format)

        image: Image = self.entity_mapper.create_image(
            name=command.name,
            title=command.title,
            description=command.description,
            media_type=media_type.value,
            size=command.file.size,
            height=image_metadata.height,
            width=image_metadata.width,
        )

        await self.s3_client.upload_fileobj(
            content_uid=image.uid,
            bucket_name=Bucket.IMAGE.value,
            fileobj=command.file,
            content_type=media_type,
        )
        url: str = await self.s3_client.generate_presigned_url(
            client_method=ClientMethod.GET_OBJECT.value,
            params={
                'Bucket': Bucket.IMAGE.value,
                'Key': str(image.uid),
            },
            http_method='GET'
        )
        image_schema = ImageCreateDto(
            uid=image.uid,
            name=image.name.as_generic_type(),
            description=command.description,
            height=image_metadata.height,
            width=image_metadata.width,
            size=command.file.size,
            media_type=media_type.value,
            nsfw=command.nsfw,
            added_by=command.user_uid,
            tags=command.tags,
            access_roles=command.access_roles,
            title=command.title,
            author=command.author,
            language=command.language,
        )

        await self.image_repository.create(create_schema=image_schema)
        await self.image_repository.session.commit()

        result = UploadImageResult(
            uid=image.uid,
            url=url,
            width=image_metadata.width,
            height=image_metadata.height,
            size=command.file.size,
            content_type=media_type.value,
            name=image.name.as_generic_type(),
            description=command.description,
            nsfw=command.nsfw,
            tags=command.tags,
            title=command.title,
            author=command.author,
            language=command.language,
        )

        event = CreateImageEvent(
            uid=image.uid,
            name=command.name,
            description=command.description,
            size=command.file.size,
            media_type=media_type.value,
            nsfw=command.nsfw,
            added_by=command.user_uid,
            tags=command.tags,
            access_roles=command.access_roles,
            title=command.title,
            language=command.language,
        )

        await self.broker.publish(message=event, queue=CREATE_IMAGE)

        return result
