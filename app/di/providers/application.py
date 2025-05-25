from dishka import Provider, Scope, provide

from application.api.v1.image.mappers import (
    CreateUploadCommandMapper,
    CreateUpdateCommandMapper,
)


class MappersApplicationProvider(Provider):
    @provide(scope=Scope.APP)
    def upload_command_mapper(self) -> CreateUploadCommandMapper:
        mapper = CreateUploadCommandMapper()
        return mapper

    @provide(scope=Scope.APP)
    def update_command_mapper(self) -> CreateUpdateCommandMapper:
        mapper = CreateUpdateCommandMapper()
        return mapper
