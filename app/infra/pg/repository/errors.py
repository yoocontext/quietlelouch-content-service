from dataclasses import dataclass
from uuid import UUID

from domain.exceptions import ApplicationException


class BaseRepositoryException(ApplicationException):
    @property
    def message(self) -> str:
        return "Repository error"


@dataclass
class ObjectNotFoundException(BaseRepositoryException):
    required_obj: UUID

    @property
    def message(self) -> str:
        return fr"Object {self.required_obj} not exists"