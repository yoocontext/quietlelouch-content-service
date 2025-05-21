from .base import BaseEntity
from ..values.content.common import NameAuthorValue, BioAuthorValue


class Author(BaseEntity):
    name: NameAuthorValue
    bio: BioAuthorValue | None
