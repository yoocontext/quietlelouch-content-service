from uuid import UUID

from sqlalchemy import select

from infra.pg.dao.base import BaseDao
from infra.pg.models import AuthorOrm
from infra.pg.dao.exceptions import ObjectNotFoundException, MissingRequiredFieldException


class AuthorDao(BaseDao):
    async def get_by_uid(self, uid: UUID) -> AuthorOrm:
        author_orm: AuthorOrm | None = await self.session.get(AuthorOrm, uid)
        if author_orm:
            return author_orm
        else:
            raise ObjectNotFoundException(required_obj=uid)

    async def get_by_name(self, name: str) -> AuthorOrm:
        result = await self.session.execute(
            select(AuthorOrm)
            .where(AuthorOrm.name == name)
        )
        author_orm: AuthorOrm | None = result.scalar_one_or_none()
        if author_orm:
            return author_orm
        else:
            raise MissingRequiredFieldException(required_field=name)
