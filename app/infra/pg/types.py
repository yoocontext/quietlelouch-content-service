from typing import Annotated
from uuid import UUID

UserUid = Annotated[UUID, "foreign key to UserOrm from User Service"]
SizeInBytes = Annotated[int, "Size in bytes"]
