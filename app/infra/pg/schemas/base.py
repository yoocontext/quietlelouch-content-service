from abc import ABC
from dataclasses import dataclass


class BaseInfraSchema(ABC):
    ...


@dataclass
class BaseUpdateInfraSchema(BaseInfraSchema):
    _fields_set: set[str]
