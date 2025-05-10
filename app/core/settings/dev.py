from functools import lru_cache
from pathlib import Path

from dotenv import dotenv_values

from core.settings.base import (
    CommonSettings,
    PgSettings,
    RmqSettings, MinioSettings,
)


class DevSettings(CommonSettings):
    def __init__(self, **data):
        env_file = Path(__file__).resolve().parents[3] / ".dev.env"
        env_data = dotenv_values(env_file)

        data["pg"] = PgSettings.model_validate(env_data)
        data["rmq"] = RmqSettings.model_validate(env_data)
        data["minio"] = MinioSettings.model_validate(env_data)

        super().__init__(**data)


@lru_cache(1)
def get_settings() -> DevSettings:
    return DevSettings()

