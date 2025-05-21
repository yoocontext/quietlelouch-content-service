from dataclasses import dataclass
from enum import Enum

from .base import BaseValue
from .exceptions import TextTooLongException, TextTooShortException, MediaTypeNotExistException


@dataclass
class NameValue(BaseValue[str, str]):
    max_len = 255
    min_len = 2

    def validate(self):
        len_value: int = len(self.value)

        if len_value < self.min_len:
            raise TextTooShortException(text=self.value, min_len=self.min_len)

        if len_value > self.max_len:
            raise TextTooLongException(text=self.value, max_len=self.max_len)

    def as_generic_type(self) -> str:
        return str(self.value)


@dataclass
class DescriptionValue(BaseValue[str, str]):
    max_len = 255
    min_len = 2

    def validate(self):
        len_value: int = len(self.value)

        if len_value < self.min_len:
            raise TextTooShortException(text=self.value, min_len=self.min_len)

        if len_value > self.max_len:
            raise TextTooLongException(text=self.value, max_len=self.max_len)

    def as_generic_type(self) -> str:
        return str(self.value)


@dataclass
class TitleValue(BaseValue[str, str]):
    max_len = 255
    min_len = 2

    def validate(self):
        len_value: int = len(self.value)

        if len_value < self.min_len:
            raise TextTooShortException(text=self.value, min_len=self.min_len)

        if len_value > self.max_len:
            raise TextTooLongException(text=self.value, max_len=self.max_len)

    def as_generic_type(self) -> str:
        return str(self.value)


class MediaType(Enum):
    JPEG = "image/jpeg"
    PNG = "image/png"
    GIF = "image/gif"
    MP4 = "video/mp4"


@dataclass
class MediaTypeValue(BaseValue[str, MediaType]):
    def validate(self):
        try:
            MediaType(self.value)
        except ValueError:
            raise MediaTypeNotExistException(media_type=self.value)

    def as_generic_type(self) -> MediaType:
        media_type = MediaType(self.value)
        return media_type