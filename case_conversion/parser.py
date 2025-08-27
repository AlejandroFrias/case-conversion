from dataclasses import dataclass

from case_conversion.unicode_char import is_separator_char, is_upper_char
from case_conversion.acronym import (
    advanced_acronym_detection,
    normalize_acronyms,
    simple_acronym_detection,
)


@dataclass
class ParsedWord:
    original_word: str
    normalized_word: str


def segment_string(string: str) -> list[str | None]:
    """Split the string into a list of strings
    Segments are formed by breaking on capital letters and non-alphanumeric separators.
    Separators are normalized to None within the list.

    >>> segment_string('FOO_bar')
    ['F', 'O', 'O', None, 'bar']

    Arguments:
        string (str): The string to process

    Returns:
        list[str]: List of words the string got minced to
    """
    words: list[str | None] = []
    separator = ""

    # curr_index of current character. Initially 1 because we don't
    # want to check if the 0th character is a boundary.
    curr_i = 1
    # Index of first character in a sequence
    seq_i = 0
    # Previous character.
    prev_i = string[0:1]

    # Treat an all-caps string as lower-case, to prevent its
    # letters to be counted as boundaries
    was_upper = False
    if string.isupper():
        string = string.lower()
        was_upper = True

    # Iterate over each character, checking for boundaries, or places
    # where the string should divided.
    while curr_i <= len(string):
        char = string[curr_i : curr_i + 1]
        split = False
        if curr_i < len(string):
            # Detect upper-case letter as boundary.
            if is_upper_char(char):
                split = True
            # Detect transition from separator to not separator.
            elif not is_separator_char(char) and is_separator_char(prev_i):
                split = True
            # Detect transition not separator to separator.
            elif is_separator_char(char) and not is_separator_char(prev_i):
                split = True
        else:
            # The loop goes one extra iteration so that it can
            # handle the remaining text after the last boundary.
            split = True

        if split:
            if not is_separator_char(prev_i):
                words.append(string[seq_i:curr_i])
            else:
                # string contains at least one separator.
                # Use the first one as the string's primary separator.
                if not separator:
                    separator = string[seq_i : seq_i + 1]

                # Use None to indicate a separator in the word list.
                words.append(None)
                # If separators weren't included in the list, then breaks
                # between upper-case sequences ("AAA_BBB") would be
                # disregarded; the letter-run detector would count them
                # as a single sequence ("AAABBB").
            seq_i = curr_i

        curr_i += 1
        prev_i = char

    if was_upper:
        words = [word.upper() if word else None for word in words]
    return words


def parse_into_words(
    string: str,
    acronyms: list[str] | None = None,
) -> list[ParsedWord]:
    """Split a string into words, normalizing their values while respecting acronyms
    for easy recombination into the various cases.

    The normalization is to capitalized words and all cap acronyms.
    The original word is also retained for certain cases that preserve the original
    words' capitalization.

    Args:
        string (str): Input string to be converted
        acronyms (optional, list of str): List of acronyms to honor
        preserve_case (bool): Whether to preserve case of acronym

    Returns:
        list[ParsedWord]: list of parsed words (normalized and original) ready
                          to be combined into the desired case

    Examples:
        >>> words = parse_into_words("hello_world")
        >>> [word.normalized_word for word in words]
        ['Hello', 'World']
        >>> [word.original_word for word in words]
        ['hello', 'world']
        >>> words = parse_into_words("helloHTMLWorld", ["HTML"])
        >>> [word.normalized_word for word in words]
        ['Hello', 'HTML', 'World']
        >>> [word.original_word for word in words]
        ['hello', 'HTML', 'World']
    """
    words_with_sep = segment_string(string.strip())

    if acronyms:
        # Use advanced acronym detection with list
        acronyms = normalize_acronyms(acronyms)
        check_acronym = advanced_acronym_detection
    else:
        acronyms = []
        # Fallback to simple acronym detection.
        check_acronym = simple_acronym_detection

    # Letter-run detector

    # Index of current word.
    i = 0
    # Index of first letter in run.
    s = None

    # Find runs of single upper-case letters.
    word = None
    while i < len(words_with_sep):
        word = words_with_sep[i]
        if word is not None and is_upper_char(word):
            if s is None:
                s = i
        elif s is not None:
            i = check_acronym(s, i, words_with_sep, acronyms) + 1
            s = None
        i += 1

    if s is not None:
        check_acronym(s, i, words_with_sep, acronyms)

    # Handle case where the entire string is all caps with no separators,
    # but there are possibly acronyms to detect within it.
    if len(words_with_sep) == 1:
        check_acronym(0, 1, words_with_sep, acronyms)

    # Separators are no longer needed, so they should be removed.
    words: list[str] = [w for w in words_with_sep if w is not None]

    def normalize_word(word: str, acronyms: list[str]) -> str:
        """Normalize word to capitalized or, for acronyms, all caps"""
        if word.upper() in acronyms:
            return word.upper()
        else:
            return word.capitalize()

    return [
        ParsedWord(original_word=word, normalized_word=normalize_word(word, acronyms))
        for word in words
    ]
