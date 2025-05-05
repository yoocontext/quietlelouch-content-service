from functools import lru_cache

from dishka import make_async_container, AsyncContainer

from .providers import (
    SettingsProvider,
    FastStreamProvider,
)


@lru_cache(1)
async def get_container() -> AsyncContainer:
    container: AsyncContainer = make_async_container(
        SettingsProvider(),
        FastStreamProvider(),
    )
    return container
