from enum import Enum, auto


class InvalidAcronymError(Exception):
    """Raise when acronym fails validation."""

    def __init__(self, acronym: str) -> None:  # noqa: D107
        msg = f"Case Conversion: acronym '{acronym}' is invalid."
        super().__init__(msg)


class Case(Enum):
    """Enum representing case types.

    Members:
        UNKNOWN: String contains no words.
        UPPER: All words are upper-case.
        LOWER: All words are lower-case.
        PASCAL: All words are title- or upper-case. (String may still
         have separators.)
        CAMEL: First word is lower-case, the rest are title- or
         upper-case. (String may still have separators.)
        MIXED: Any other mixing of word casing. Never occurs if there
         are no separators.
    """

    UNKNOWN = auto()
    UPPER = auto()
    LOWER = auto()
    CAMEL = auto()
    PASCAL = auto()
    MIXED = auto()
