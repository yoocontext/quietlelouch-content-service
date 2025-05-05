from typing import AsyncIterable

from dishka import Provider, Scope, provide
from faststream.rabbit import RabbitBroker
from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    create_async_engine,
    async_sessionmaker,
)

from core.settings.base import CommonSettings


class FastStreamProvider(Provider):
    @provide(scope=Scope.APP)
    async def create_broker(self, settings: CommonSettings) -> AsyncIterable[RabbitBroker]:
        async with RabbitBroker(url=settings.rmq.rabbit_broker_url) as broker:
            yield broker


class DatabaseProvider(Provider):
    @provide(scope=Scope.APP)
    async def create_engine(self, settings: CommonSettings) -> AsyncEngine:
        return create_async_engine(
            url=settings.pg.postgres_url,
            echo=False,
        )

    @provide(scope=Scope.APP)
    async def create_session_maker(
        self, engine: AsyncEngine
    ) -> async_sessionmaker[AsyncSession]:
        return async_sessionmaker(bind=engine, autoflush=False, expire_on_commit=False)

    @provide(scope=Scope.REQUEST, provides=AsyncSession)
    async def provide_session(
        self, sessionmaker: async_sessionmaker[AsyncSession]
    ) -> AsyncIterable[AsyncSession]:
        async with sessionmaker() as session:
            yield session
