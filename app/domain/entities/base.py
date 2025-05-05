from dataclasses import dataclass, field
from uuid import uuid4, UUID

@dataclass(kw_only=True)
class BaseEntity:
    uid: UUID = field(default_factory=uuid4)
