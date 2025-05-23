from dataclasses import dataclass
from uuid import UUID

from faststream.rabbit import RabbitBroker

from domain.logic.use_cases import BaseUseCase, BaseCommand, BaseResult
from infra.pg.repository import ImageRepository
from infra.rmq.events import DeleteImageEvent
from infra.rmq.queues import DELETE_IMAGE
from infra.s3.boto_client import BotoClient
from infra.s3.const import Bucket


@dataclass
class DeleteImageCommand(BaseCommand):
    image_uid: UUID


@dataclass
class DeleteImageResult(BaseResult):
    pass


@dataclass
class DeleteImageUseCase(BaseUseCase):
    s3_client: BotoClient
    broker: RabbitBroker
    repository: ImageRepository

    async def act(self, command: DeleteImageCommand) -> DeleteImageResult:
        # todo валидировать роль

        await self.repository.delete(uid=command.image_uid)
        await self.s3_client.delete_content(content_uid=command.image_uid, bucket_name=Bucket.IMAGE.value)

        event = DeleteImageEvent(uid=command.image_uid)
        await self.broker.publish(message=event, queue=DELETE_IMAGE)

        await self.repository.session.commit()

        return DeleteImageResult()
