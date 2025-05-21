from dishka import Provider, Scope, provide

from domain.mappers import (
    ContentEntityMapper,
    ContentValuesMapper
)


class MappersDomainProvider(Provider):
    @provide(scope=Scope.APP)
    def create_entity(self, values_mapper: ContentValuesMapper) -> ContentEntityMapper:
        mapper = ContentEntityMapper(values_mapper=values_mapper)
        return mapper

    @provide(scope=Scope.APP)
    def create_value(self) -> ContentValuesMapper:
        mapper = ContentValuesMapper()
        return mapper
