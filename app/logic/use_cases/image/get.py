from dataclasses import dataclass, field
from typing import Annotated
from uuid import UUID

from domain.logic.use_cases import BaseUseCase, BaseCommand, BaseResult
from infra.pg.dao.image import ImageDao
from infra.pg.models import ImageOrm
from infra.s3.boto_client import BotoClient
from infra.s3.const import Bucket, ClientMethod


@dataclass
class GetImageCommand(BaseCommand):
    image_uid: UUID


@dataclass(kw_only=True)
class GetImageResult(BaseResult):
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
class GetImageUseCase(BaseUseCase):
    s3_client: BotoClient
    image_dao: ImageDao

    async def act(self, command: GetImageCommand) -> GetImageResult:
        # todo валидировать роль

        image_orm: ImageOrm = await self.image_dao.get(uid=command.image_uid)
        tags: set[str] = {tag.name for tag in image_orm.tags}

        url: str = await self.s3_client.generate_presigned_url(
            client_method=ClientMethod.GET_OBJECT.value,
            params={
                'Bucket': Bucket.IMAGE.value,
                'Key': str(image_orm.uid),
            },
            http_method='GET'
        )

        title: str | None = image_orm.title.name if image_orm.title else None
        author: str | None = image_orm.author.name if image_orm.author else None
        language: str | None = image_orm.language.name if image_orm.language else None

        result = GetImageResult(
            uid=image_orm.uid,
            url=url,
            name=image_orm.name,
            description=image_orm.description,
            nsfw=image_orm.nsfw,
            tags=tags,
            title=title,
            author=author,
            language=language,
            width=image_orm.width,
            height=image_orm.height,
            size=image_orm.size,
            content_type=image_orm.media_type,
        )
        return result
