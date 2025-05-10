from dataclasses import dataclass
from uuid import UUID

from domain.entities.content import MediaType
from domain.logic.use_cases import BaseUseCase, BaseCommand, BaseResult
from infra.s3.base import S3GetObjectResponse
from infra.s3.boto_client import BotoClient


@dataclass
class GetContentCommand(BaseCommand):
    content_uid: UUID


@dataclass
class GetContentResult(BaseResult):
    media_type: MediaType


@dataclass
class GetContentUseCase(BaseUseCase):
    s3_client: BotoClient

    async def act(self, command: GetContentCommand) -> GetContentResult:
        # todo добавить роли
        response: S3GetObjectResponse = await self.s3_client.get_content(content_uid=command.content_uid)



