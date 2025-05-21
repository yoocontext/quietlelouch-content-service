from uuid import UUID

from sqlalchemy import select

from infra.pg.models import TitleOrm
from infra.pg.repository.common.base import BaseRepository
from infra.pg.repository.common.exceptions import ObjectNotFoundException, MissingRequiredFieldException


class TitleRepository(BaseRepository):
    async def get_by_uid(self, uid: UUID) -> TitleOrm:
        title_orm: TitleOrm | None = await self.session.get(TitleOrm, uid)
        if title_orm:
            return title_orm
        else:
            raise ObjectNotFoundException(required_obj=uid)

    async def get_by_name(self, name: str) -> TitleOrm:
        result = await self.session.execute(
            select(TitleOrm)
            .where(TitleOrm.name == name)
        )
        title_orm: TitleOrm | None = result.scalar_one_or_none()
        if title_orm:
            return title_orm
        else:
            raise MissingRequiredFieldException(required_field=name)
