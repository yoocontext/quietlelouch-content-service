from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class RmqSettings(BaseSettings):
    model_config = SettingsConfigDict(extra="allow")

    username: str = Field(alias="RMQ_USERNAME", default="RMQ_USERNAME")
    password: str = Field(alias="RMQ_PASSWORD", default="RMQ_PASSWORD")
    host: str = Field(alias="RMQ_HOST", default="localhost")
    port: int = Field(alias="RMQ_PORT", default=5672)

    @property
    def rabbit_broker_url(self) -> str:
        return rf"amqp://{self.username}:{self.password}@{self.host}:{self.port}/"


class PgSettings(BaseSettings):
    model_config = SettingsConfigDict(extra="allow")

    db: str = Field(alias="POSTGRES_NAME", default="POSTGRES_NAME")
    user: str = Field(alias="POSTGRES_USER", default="POSTGRES_USER")
    password: str = Field(alias="POSTGRES_PASSWORD", default="POSTGRES_PASSWORD")
    host: str = Field(alias="POSTGRES_HOST", default="POSTGRES_HOST")
    port: str = Field(alias="POSTGRES_PORT", default="POSTGRES_PORT")

    @property
    def postgres_url(self) -> str:
        return rf"postgresql+asyncpg://{self.user}:{self.password}@{self.host}:{self.port}/{self.db}"


class MinioSettings(BaseSettings):
    model_config = SettingsConfigDict(extra="allow")

    aws_access_key_id: str = Field(alias="AWS_ACCESS_KEY_ID", default="AWS_ACCESS_KEY_ID")
    aws_secret_access_key: str = Field(alias="AWS_SECRET_ACCESS_KEY", default="AWS_SECRET_ACCESS_KEY")
    endpoint_url: str = Field(alias="ENDPOINT_URL", default="ENDPOINT_URL")


class CommonSettings(BaseSettings):
    pg: PgSettings
    rmq: RmqSettings
    minio: MinioSettings

