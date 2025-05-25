from dishka import Provider, Scope, provide
from sqlalchemy.ext.asyncio import AsyncSession

from infra.pg.dao import (
    TagDao,
    RoleDao,
    TitleDao,
    AuthorDao,
    LanguageDao,
    ImageDao,
)


class DaoProvider(Provider):
    @provide(scope=Scope.REQUEST)
    def create_tag(self, session: AsyncSession) -> TagDao:
        return TagDao(session=session)

    @provide(scope=Scope.REQUEST)
    def create_role(self, session: AsyncSession) -> RoleDao:
        return RoleDao(session=session)

    @provide(scope=Scope.REQUEST)
    def create_title(self, session: AsyncSession) -> TitleDao:
        return TitleDao(session=session)

    @provide(scope=Scope.REQUEST)
    def create_author(self, session: AsyncSession) -> AuthorDao:
        return AuthorDao(session=session)

    @provide(scope=Scope.REQUEST)
    def create_language(self, session: AsyncSession) -> LanguageDao:
        return LanguageDao(session=session)

    @provide(scope=Scope.REQUEST)
    def create_image(self, session: AsyncSession) -> ImageDao:
        return ImageDao(session=session)
