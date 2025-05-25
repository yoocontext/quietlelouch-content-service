from functools import lru_cache

from dishka import make_async_container, AsyncContainer

from .providers import (
    SettingsProvider,
    FastStreamProvider,
    DatabaseProvider,
    Boto3Provider,
    RepositoryProvider,
    MappersDomainProvider,
    MappersApplicationProvider,
    ImageUseCaseProvider,
    MetadataProvider,
    MediaTypeProvider,
    PgMapperProvider,
    DaoProvider,
)


@lru_cache(1)
def get_container() -> AsyncContainer:
    container: AsyncContainer = make_async_container(
        SettingsProvider(),
        FastStreamProvider(),
        DatabaseProvider(),
        Boto3Provider(),
        RepositoryProvider(),
        MappersDomainProvider(),
        MappersApplicationProvider(),
        ImageUseCaseProvider(),
        MetadataProvider(),
        MediaTypeProvider(),
        PgMapperProvider(),
        DaoProvider(),
    )
    return container
