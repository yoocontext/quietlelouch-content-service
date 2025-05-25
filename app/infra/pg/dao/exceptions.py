from collections.abc import Iterable
from dataclasses import dataclass
from uuid import UUID

from domain.exceptions import InfraException


class BaseDaoException(InfraException):
    @property
    def message(self) -> str:
        return "Repository error"


@dataclass
class ObjectNotFoundException(BaseDaoException):
    required_obj: UUID

    @property
    def message(self) -> str:
        return fr"Object {self.required_obj} not exist"


@dataclass
class MissingRequiredFieldException(BaseDaoException):
    required_field: str | Iterable

    @property
    def message(self) -> str:
        if isinstance(self.required_field, str):
            fields_str = self.required_field
        elif isinstance(self.required_field, Iterable):
            fields_str = ", ".join(str(f) for f in self.required_field)
        else:
            fields_str = str(self.required_field)

        return fr"Missing required field(s): {fields_str}"