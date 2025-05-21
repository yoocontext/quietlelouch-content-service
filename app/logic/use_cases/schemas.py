from dataclasses import dataclass


@dataclass
class TagCreateCaseSchema:
    name: str
    description: str | None


@dataclass
class RoleCreateCaseSchema:
    name: str
    description: str | None


@dataclass
class TitleCreateCaseSchema:
    name: str


@dataclass
class AuthorCreateCaseSchema:
    name: str
    bio: str | None


@dataclass
class LanguageCreateCaseSchema:
    name: str
    description: str | None