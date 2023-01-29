from enum import Enum, unique


@unique
class Status(Enum):
    """Status is the enum with the Cards API types."""

    ALL = "all"
    ACTIVE = "active"
    RENEWED = "renewed"
