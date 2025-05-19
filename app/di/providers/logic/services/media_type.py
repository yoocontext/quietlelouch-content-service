from dishka import Provider, Scope, provide

from logic.services.content.media_type import GetMediaTypeService


class MediaTypeProvider(Provider):
    @provide(scope=Scope.APP)
    def create_content_type(self) -> GetMediaTypeService:
        service = GetMediaTypeService()
        return service
