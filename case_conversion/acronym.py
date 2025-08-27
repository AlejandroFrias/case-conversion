from typing import Iterator, TypeGuard

from case_conversion.unicode_char import is_separator_char


class InvalidAcronymError(Exception):
    """Raise when acronym fails validation."""

    def __init__(self, acronym: str) -> None:  # noqa: D107
        msg = f"Case Conversion: acronym '{acronym}' is invalid."
        super().__init__(msg)


def find_substring_ranges(string: str, substring: str) -> Iterator[tuple[int, int]]:
    """Finds (start, end) ranges of all occurrences of substring in string.

    >>> list(find_substring_ranges("foo_bar_bar", "bar"))
    [(4, 7), (8, 11)]
    """
    start = 0
    sub_len = len(substring)
    while True:
        start = string.find(substring, start)
        if start == -1:
            return
        yield (start, start + sub_len)
        start += 1


def is_str_list(a_list: list[str | None]) -> TypeGuard[list[str]]:
    return all(isinstance(item, str) for item in a_list)


def advanced_acronym_detection(
    s: int, i: int, words: list[str | None], acronyms: list[str]
) -> int:
    """Detect acronyms by checking against a list of acronyms.

    Arguments:
        s (int): Index of first word in run
        i (int): Index of current word
        words (list of str): Segmented input string
        acronyms (list of str): List of acronyms

    Returns:
        int: Index of last word in run
    """
    # Combine each letter into single string.
    words_to_join = words[s:i]
    assert is_str_list(words_to_join)
    acr_str = "".join(words_to_join)

    # List of ranges representing found acronyms.
    range_list: list[tuple[int, int]] = []
    # Set of remaining letters.
    not_range = set(range(len(acr_str)))

    # Search for each acronym in acr_str.
    for acr in acronyms:
        for start, end in find_substring_ranges(acr_str, acr):
            # Make sure found acronym doesn't overlap with others.
            for r in range_list:
                if start < r[1] and end > r[0]:
                    break
            else:
                range_list.append((start, end))
                for j in range(start, end):
                    not_range.remove(j)

    # Add remaining letters as ranges.
    if not_range:
        not_range = sorted(not_range)
        start_nr = not_range[0] if not_range else -1
        prev_nr = start_nr - 1
        for nr in sorted(not_range):
            if nr > prev_nr + 1:
                range_list.append((start_nr, prev_nr + 1))
                start_nr = nr
            prev_nr = nr
        range_list.append((start_nr, prev_nr + 1))

    # No ranges will overlap, so it's safe to sort by lower bound,
    # which sort() will do by default.
    range_list.sort()

    # Remove original letters in word list.
    for _ in range(s, i):
        del words[s]

    # Replace them with new word grouping.
    for j in range(len(range_list)):
        r = range_list[j]
        words.insert(s + j, acr_str[r[0] : r[1]])

    return s + len(range_list) - 1


def simple_acronym_detection(s: int, i: int, words: list[str | None], *args) -> int:
    """Detect acronyms based on runs of upper-case letters.

    Arguments:
        s (int): Index of first letter in run
        i (int): Index of current word
        words (list of str): Segmented input string
        args: Placeholder to conform to signature of
            advanced_acronym_detection

    Returns:
        int: Index of last letter in run
    """
    # Combine each letter into a single string.
    words_to_join = words[s:i]
    assert is_str_list(words_to_join)
    acr_str = "".join(words_to_join)

    # Remove original letters in word list.
    for _ in range(s, i):
        del words[s]

    # Replace them with new word grouping.
    words.insert(s, "".join(acr_str))

    return s


def is_valid_acronym(a_string: str) -> bool:
    if not a_string:
        return False

    for a_char in a_string:
        if is_separator_char(a_char):
            return False

    return True


def normalize_acronyms(unsafe_acronyms: list[str]) -> list[str]:
    """Validates and normalizes acronyms to upper-case.

    Arguments:
        unsafe_acronyms (list of str): Acronyms to be sanitized

    Returns:
        list of str: Sanitized acronyms

    Raises:
        InvalidAcronymError: Upon encountering an invalid acronym
    """
    acronyms = []
    for acr in unsafe_acronyms:
        if not is_valid_acronym(acr):
            raise InvalidAcronymError(acr)
        acronyms.append(acr.upper())
    return acronyms
