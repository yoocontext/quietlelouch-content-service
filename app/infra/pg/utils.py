from typing import TypeVar

from infra.pg.models import BaseOrm
from infra.pg.schemas.base import BaseUpdateInfraSchema


MO = TypeVar("MO", bound=BaseOrm)

def update_orm(schema: BaseUpdateInfraSchema, orm: MO) -> MO:
    for field in schema._fields_set:
        if hasattr(orm, field):
            value = getattr(schema, field)
            setattr(orm, field, value)
    return orm