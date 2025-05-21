from dishka import Provider, Scope, provide
from sqlalchemy.ext.asyncio import AsyncSession

from infra.pg.mappers import ContentOrmToEntityMapper
from infra.pg.repository import (
    AuthorRepository,
    RoleRepository,
    TagRepository,
    ImageRepository,
    TitleRepository,
    LanguageRepository,
)


class RepositoryProvider(Provider):
    @provide(scope=Scope.REQUEST)
    def create_image(
        self,
        session: AsyncSession,
        tag_repository: TagRepository,
        role_repository: RoleRepository,
        title_repository: TitleRepository,
        author_repository: AuthorRepository,
        language_repository: LanguageRepository,
        orm_mapper: ContentOrmToEntityMapper,
    ) -> ImageRepository:
        repo = ImageRepository(
            session=session,
            tag_repository=tag_repository,
            role_repository=role_repository,
            title_repository=title_repository,
            author_repository=author_repository,
            language_repository=language_repository,
            orm_mapper=orm_mapper,
        )
        return repo


    @provide(scope=Scope.REQUEST)
    def create_author(self, session: AsyncSession) -> AuthorRepository:
        repo = AuthorRepository(session=session)
        return repo

    @provide(scope=Scope.REQUEST)
    def create_role(self, session: AsyncSession) -> RoleRepository:
        repo = RoleRepository(session=session)
        return repo

    @provide(scope=Scope.REQUEST)
    def create_tag(self, session: AsyncSession) -> TagRepository:
        repo = TagRepository(session=session)
        return repo

    @provide(scope=Scope.REQUEST)
    def create_title(self, session: AsyncSession) -> TitleRepository:
        repo = TitleRepository(session=session)
        return repo

    @provide(scope=Scope.REQUEST)
    def create_author(self, session: AsyncSession) -> AuthorRepository:
        repo = AuthorRepository(session=session)
        return repo

    @provide(scope=Scope.REQUEST)
    def create_language(self, session: AsyncSession) -> LanguageRepository:
        repo = LanguageRepository(session=session)
        return repo