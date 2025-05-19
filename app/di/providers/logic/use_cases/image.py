from dishka import Provider, Scope, provide

from domain.mappers import ContentEntityMapper
from infra.pg.repository import ImageRepository
from infra.s3.boto_client import BotoClient
from logic.services.content.media_type import GetMediaTypeService
from logic.services.content.metadata import GetPictureMetadataService
from logic.use_cases.image import UploadImageUseCase


class ImageUseCaseProvider(Provider):
    @provide(scope=Scope.REQUEST)
    def create_upload(
        self,
        image_meta_service: GetPictureMetadataService,
        get_media_type_service: GetMediaTypeService,
        entity_mapper: ContentEntityMapper,
        s3_client: BotoClient,
        image_repository: ImageRepository,
    ) -> UploadImageUseCase:
        case = UploadImageUseCase(
            image_meta_service=image_meta_service,
            get_media_type_service=get_media_type_service,
            entity_mapper=entity_mapper,
            s3_client=s3_client,
            image_repository=image_repository,
        )
        return case