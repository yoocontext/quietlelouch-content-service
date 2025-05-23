from dataclasses import dataclass
from uuid import UUID

from faststream.rabbit import RabbitBroker

from domain.logic.use_cases import BaseUseCase, BaseCommand, BaseResult
from infra.rmq.events import ImageDeleteEvent
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

    async def act(self, command: DeleteImageCommand) -> DeleteImageResult:
        # todo валидировать роль

        await self.s3_client.delete_content(content_uid=command.image_uid, bucket_name=Bucket.IMAGE.value)

        event = ImageDeleteEvent(uid=command.image_uid)
        await self.broker.publish(message=event, queue=DELETE_IMAGE)

        return DeleteImageResult()
