from abc import ABC, abstractmethod


class ApplicationException(ABC, Exception):
    @property
    @abstractmethod
    def message(self) -> str:
        return "Application exception"