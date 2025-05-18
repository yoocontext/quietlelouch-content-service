from dataclasses import dataclass
from typing import ClassVar

from domain.values.base import BaseValue
from domain.values.exceptions import (
    TextTooLongException,
    TextTooShortException,
)


@dataclass
class NameAuthorValue(BaseValue[str, str]):
    max_len: ClassVar[int] = 13
    min_len: ClassVar[int] = 2

    def validate(self):
        len_value: int = len(self.value)

        if len_value < self.min_len:
            raise TextTooShortException(text=self.value, min_len=self.min_len)

        if len_value > self.max_len:
            raise TextTooLongException(text=self.value, max_len=self.max_len)

    def as_generic_type(self) -> str:
        return str(self.value)


@dataclass
class BioAuthorValue(BaseValue[str, str]):
    max_len: ClassVar[int] = 255
    min_len: ClassVar[int] = 0

    def validate(self):
        len_value: int = len(self.value)

        if len_value < self.min_len:
            raise TextTooShortException(text=self.value, min_len=self.min_len)

        if len_value > self.max_len:
            raise TextTooLongException(text=self.value, max_len=self.max_len)

    def as_generic_type(self) -> str:
        return str(self.value)