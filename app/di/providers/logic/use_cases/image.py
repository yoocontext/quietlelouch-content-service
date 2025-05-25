from dishka import Provider, Scope, provide
from faststream.rabbit import RabbitBroker

from domain.mappers import ContentEntityMapper
from infra.pg.dao import ImageDao
from infra.pg.repository import ImageRepository
from infra.s3.boto_client import BotoClient
from logic.services.meta.media_type import GetMediaTypeService
from logic.services.meta.metadata import GetPictureMetadataService
from logic.use_cases.image.update import UpdateImageUseCase
from logic.use_cases.image.upload import UploadImageUseCase
from logic.use_cases.image.get import GetImageUseCase
from logic.use_cases.image.delete import DeleteImageUseCase


class ImageUseCaseProvider(Provider):
    @provide(scope=Scope.REQUEST)
    def create_upload(
        self,
        image_meta_service: GetPictureMetadataService,
        get_media_type_service: GetMediaTypeService,
        entity_mapper: ContentEntityMapper,
        s3_client: BotoClient,
        image_repository: ImageRepository,
        broker: RabbitBroker,
    ) -> UploadImageUseCase:
        case = UploadImageUseCase(
            image_meta_service=image_meta_service,
            get_media_type_service=get_media_type_service,
            entity_mapper=entity_mapper,
            s3_client=s3_client,
            image_repository=image_repository,
            broker=broker,
        )
        return case

    @provide(scope=Scope.REQUEST)
    def create_get(
        self,
        s3_client: BotoClient,
        image_dao: ImageDao,
    ) -> GetImageUseCase:
        case = GetImageUseCase(
            s3_client=s3_client,
            image_dao=image_dao,
        )
        return case

    @provide(scope=Scope.REQUEST)
    def create_delete(
        self,
        s3_client: BotoClient,
        broker: RabbitBroker,
        repository: ImageRepository
    ) -> DeleteImageUseCase:
        use_case = DeleteImageUseCase(
            s3_client=s3_client,
            broker=broker,
            repository=repository,
        )
        return use_case

    @provide(scope=Scope.REQUEST)
    def create_update(
        self,
        image_repository: ImageRepository,
        image_dao: ImageDao,
        s3_client: BotoClient,
    ) -> UpdateImageUseCase:
        case = UpdateImageUseCase(
            image_repository=image_repository,
            image_dao=image_dao,
            s3_client=s3_client,
        )
        return case
