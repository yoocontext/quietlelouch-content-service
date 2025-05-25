from dataclasses import dataclass

from .base import BaseEntity
from ..values.content.common import NameAuthorValue, BioAuthorValue


@dataclass
class Author(BaseEntity):
    name: NameAuthorValue
    bio: BioAuthorValue | None
