from dataclasses import dataclass
from .types import Case
from .utils import (
    advanced_acronym_detection,
    determine_case,
    is_upper,
    normalize_word,
    sanitize_acronyms,
    segment_string,
    simple_acronym_detection,
)


@dataclass
class Word:
    original_word: str
    normalized_word: str


@dataclass
class ParseData:
    words: list[Word]
    original_case: Case
    original_separator: str


def parse_case(
    string: str,
    acronyms: list[str] | None = None,
) -> ParseData:
    """Split a string into words, determine its case and separator.

    Args:
        string (str): Input string to be converted
        acronyms (optional, list of str): List of acronyms to honor
        preserve_case (bool): Whether to preserve case of acronym

    Returns:
        list of str: Segmented input string
        Case: Determined case
        str: Determined separator

    Examples:
        >>> parse_case("hello_world")
        ["Hello", "World"], Case.LOWER, "_"
        >>> parse_case("helloHTMLWorld", ["HTML"])
        ["Hello", "HTML", World"], Case.MIXED, None
        >>> parse_case("helloHtmlWorld", ["HTML"], True)
        ["Hello", "Html", World"], Case.CAMEL, None
    """
    words_with_sep, separator, was_upper = segment_string(string)

    if acronyms:
        # Use advanced acronym detection with list
        acronyms = sanitize_acronyms(acronyms)
        check_acronym = advanced_acronym_detection  # type: ignore
    else:
        acronyms = []
        # Fallback to simple acronym detection.
        check_acronym = simple_acronym_detection  # type: ignore

    # Letter-run detector

    # Index of current word.
    i = 0
    # Index of first letter in run.
    s = None

    # Find runs of single upper-case letters.
    while i < len(words_with_sep):
        word = words_with_sep[i]
        if word is not None and is_upper(word):
            if s is None:
                s = i
        elif s is not None:
            i = check_acronym(s, i, words_with_sep, acronyms) + 1  # type: ignore
            s = None
        i += 1

    # Separators are no longer needed, so they should be removed.
    words: list[str] = [w for w in words_with_sep if w is not None]

    # Determine case type.
    case_type = determine_case(was_upper, words, string)

    word_list = [
        Word(original_word=word, normalized_word=normalize_word(word, acronyms))
        for word in words
    ]

    return ParseData(
        words=word_list, original_case=case_type, original_separator=separator
    )
