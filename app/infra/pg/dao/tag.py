from sqlalchemy import select

from infra.pg.dao.base import BaseDao
from infra.pg.models import TagOrm
from infra.pg.dao.exceptions import MissingRequiredFieldException


class TagDao(BaseDao):
    async def get_by_names(self, names: set[str]) -> list[TagOrm]:
        result = await self.session.execute(
            select(TagOrm)
            .where(TagOrm.name.in_(names))
        )
        tags: list[TagOrm] = list(result.scalars().all())

        if len(tags) == len(names):
            return tags
        else:
            found_names = {tag.name for tag in tags}
            missing_names = names - found_names
            raise MissingRequiredFieldException(required_field=missing_names)
