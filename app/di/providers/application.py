from dishka import Provider, Scope, provide

from application.api.v1.image.upload.mappers import CreateUploadCommandMapper


class MappersApplicationProvider(Provider):
    @provide(scope=Scope.APP)
    def create_upload_command_mapper(self) -> CreateUploadCommandMapper:
        mapper = CreateUploadCommandMapper()
        return mapper