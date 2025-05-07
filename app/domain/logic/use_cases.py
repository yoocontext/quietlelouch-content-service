from abc import ABC, abstractmethod


class BaseCommand:
    ...


class BaseResult:
    ...


class BaseUseCase(ABC):
    @abstractmethod
    async def act(self, command: BaseCommand) -> BaseResult:
        ...
