from .base import BaseEntity
from domain.values.author import NameAuthorValue, BioAuthorValue


class Author(BaseEntity):
    name: NameAuthorValue
    bio: BioAuthorValue | None
