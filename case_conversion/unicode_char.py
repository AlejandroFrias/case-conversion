"""Unicode single character checkers"""

import unicodedata


def is_separator_char(a_char: str) -> bool:
    """Non-alphanumeric unicode character check."""
    return not (
        is_upper_char(a_char) or is_lower_char(a_char) or is_decimal_char(a_char)
    )


def is_decimal_char(a_char: str) -> bool:
    """Numeric unicode character check."""
    return len(a_char) == 1 and unicodedata.category(a_char) == "Nd"


def is_lower_char(a_char: str) -> bool:
    """Lowercase unicode character check."""
    return len(a_char) == 1 and unicodedata.category(a_char) == "Ll"


def is_upper_char(a_char: str) -> bool:
    """Uppercase unicode character check."""
    return len(a_char) == 1 and unicodedata.category(a_char) == "Lu"
