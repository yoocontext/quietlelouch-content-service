from dataclasses import dataclass
from uuid import UUID

from domain.entities.content import Image
from domain.logic.use_cases import BaseUseCase, BaseCommand, BaseResult
from infra.pg.repository.content.image import ImageRepository
from infra.s3.boto_client import BotoClient
from infra.s3.const import Bucket, ClientMethod


@dataclass
class GetImageCommand(BaseCommand):
    image_uid: UUID


@dataclass
class GetImageResult(BaseResult):
    url: str
    width: int
    height: int
    size: int
    content_type: str


@dataclass
class GetImageUseCase(BaseUseCase):
    s3_client: BotoClient
    image_repository: ImageRepository

    async def act(self, command: GetImageCommand) -> GetImageResult:
        # todo валидировать роль

        image: Image = await self.image_repository.get_by_uid(uid=command.image_uid)

        url: str = await self.s3_client.generate_presigned_url(
            client_method=ClientMethod.GET_OBJECT.value,
            params={
                'Bucket': Bucket.IMAGE.value,
                'Key': str(image.uid),
            },
            http_method='GET'
        )

        result = GetImageResult(
            url=url,
            width=image.width,
            height=image.height,
            size=image.size.as_generic_type(),
            content_type=image.media_type.value,
        )
        return result
