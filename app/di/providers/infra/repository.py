from dishka import Provider, Scope, provide
from sqlalchemy.ext.asyncio import AsyncSession

from infra.pg.mappers import ImageOrmToEntityMapper
from infra.pg.repository import (
    ImageRepository,
)
from infra.pg.dao import (
    TagDao,
    RoleDao,
    TitleDao,
    AuthorDao,
    LanguageDao,
    ImageDao,
)


class RepositoryProvider(Provider):
    @provide(scope=Scope.REQUEST)
    def create_image(
        self,
        session: AsyncSession,
        tag_dao: TagDao,
        role_dao: RoleDao,
        title_dao: TitleDao,
        author_dao: AuthorDao,
        language_dao: LanguageDao,
        image_dao: ImageDao,
        orm_mapper: ImageOrmToEntityMapper,
    ) -> ImageRepository:
        repo = ImageRepository(
            session=session,
            tag_dao=tag_dao,
            role_dao=role_dao,
            title_dao=title_dao,
            author_dao=author_dao,
            language_dao=language_dao,
            image_dao=image_dao,
            mapper=orm_mapper,
        )
        return repo
