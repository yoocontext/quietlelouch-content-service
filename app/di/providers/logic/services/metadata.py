from dishka import Provider, Scope, provide

from logic.services.meta.metadata import GetPictureMetadataService


class MetadataProvider(Provider):
    @provide(scope=Scope.APP)
    def create_picture(self) -> GetPictureMetadataService:
        service = GetPictureMetadataService()
        return service
