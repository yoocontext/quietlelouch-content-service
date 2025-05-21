from abc import ABC, abstractmethod


class ApplicationException(ABC, Exception):
    @property
    @abstractmethod
    def message(self) -> str:
        return "Application Exception"


class DomainException(ApplicationException):
    @property
    @abstractmethod
    def message(self) -> str:
        return "Domain Exception"


class InfraException(ApplicationException):
    @property
    @abstractmethod
    def message(self) -> str:
        return "Infra Exception"

class ServiceException(ApplicationException):
    @property
    @abstractmethod
    def message(self) -> str:
        return "Service Exception"