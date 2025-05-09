from typing import AsyncIterable

from aioboto3 import Session
from dishka import Provider, Scope, provide
from faststream.rabbit import RabbitBroker
from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    create_async_engine,
    async_sessionmaker,
)

from core.settings.base import CommonSettings
from infra.s3.boto_client import AsyncS3ClientProtocol, BotoClient


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


class Boto3Provider(Provider):
    @provide(scope=Scope.APP)
    def create_session(self) -> Session:
        session = Session()
        return session

    @provide(scope=Scope.REQUEST)
    async def create_client(self, session: Session, settings: CommonSettings) -> AsyncIterable[AsyncS3ClientProtocol]:
        async with session.client(service_name="s3",
            aws_access_key_id=settings.minio.aws_access_key_id,
            aws_secret_access_key=settings.minio.aws_secret_access_key,
            endpoint_url=settings.minio.endpoint_url,
        ) as client:
            yield client

    @provide(scope=Scope.REQUEST)
    def create_boto_client(self, boto3_client: AsyncS3ClientProtocol) -> BotoClient:
        client = BotoClient(
            client=boto3_client,
            bucket_name="content",
        )
        return client