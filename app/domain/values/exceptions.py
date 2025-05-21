from dataclasses import dataclass

from domain.exceptions import DomainException


class ValueException(DomainException):
    @property
    def message(self) -> str:
        return "Domain Value Exception"


@dataclass
class TextTooLongException(ValueException):
    text: str
    max_len: int

    @property
    def message(self) -> str:
        return f"Text is too long: {len(self.text)} characters (maximum allowed is {self.max_len})"


@dataclass
class TextTooShortException(ValueException):
    text: str
    min_len: int

    @property
    def message(self) -> str:
        return f"Text is too short: {len(self.text)} characters (minimum allowed is {self.min_len})"


@dataclass
class MediaTypeNotExistException(ValueException):
    media_type: str

    @property
    def message(self) -> str:
        return f"Media type: {self.media_type} does not exist"