from sqlalchemy import select

from infra.pg.dao.base import BaseDao
from infra.pg.models import RoleOrm
from infra.pg.dao.exceptions import MissingRequiredFieldException


class RoleDao(BaseDao):
    async def get_by_names(self, names: set[str]) -> list[RoleOrm]:
        result = await self.session.execute(
            select(RoleOrm)
            .where(RoleOrm.name.in_(names))
        )
        roles: list[RoleOrm] = list(result.scalars().all())

        if len(roles) == len(names):
            return roles
        else:
            found_names = {tag.name for tag in roles}
            missing_names = names - found_names
            raise MissingRequiredFieldException(required_field=missing_names)
