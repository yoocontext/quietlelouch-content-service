from dishka import Provider, Scope, provide

from domain.mappers import ContentValuesMapper
from infra.pg.mappers import ImageOrmToEntityMapper, ContentCreateSchemaToOrmMapper


class PgMapperProvider(Provider):
    @provide(scope=Scope.APP)
    def create_to_entity(self, values_mapper: ContentValuesMapper) -> ImageOrmToEntityMapper:
        mapper = ImageOrmToEntityMapper(values_mapper=values_mapper)
        return mapper

    @provide(scope=Scope.APP)
    def create_schema(self) -> ContentCreateSchemaToOrmMapper:
        mapper = ContentCreateSchemaToOrmMapper()
        return mapper