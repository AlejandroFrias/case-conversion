from typing import List, Optional, Tuple

from .types import Case
from .utils import (
    advanced_acronym_detection,
    determine_case,
    is_upper,
    normalize_words,
    sanitize_acronyms,
    segment_string,
    simple_acronym_detection,
)


def parse_case(
    string: str, acronyms: Optional[List[str]] = None, preserve_case: bool = False,
) -> Tuple[List[str], Case, str]:
    """Split a string into words, determine its case and seperator.

    Args:
        string (str): Input string to be converted
        acronyms (optional, list of str): List of acronyms to honor
        preserve_case (bool): Whether to preserve case of acronym

    Returns:
        list of str: Segmented input string
        Case: Determined case
        str: Determined seperator

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
    words: List[str] = [w for w in words_with_sep if w is not None]

    # Determine case type.
    case_type = determine_case(was_upper, words, string)

    if preserve_case:
        if was_upper:
            words = [w.upper() for w in words]
    else:
        words = normalize_words(words, acronyms)

    return words, case_type, separator


def camel(text: str, acronyms: Optional[List[str]] = None) -> str:
    """Return text in camelCase style.

    Args:
        text (str): Input string to be converted
        acronyms (optional, list of str): List of acronyms to honor

    Returns:
        str: Case converted text

    Examples:
        >>> camel("hello world")
        'helloWorld'
        >>> camel("HELLO_HTML_WORLD", ["HTML"])
        'helloHTMLWorld'
    """
    words, _case, _sep = parse_case(text, acronyms)
    if words:
        words[0] = words[0].lower()
    return "".join(words)


def pascal(text: str, acronyms: Optional[List[str]] = None) -> str:
    """Return text in PascalCase style.

    This case style is also known as: MixedCase

    Args:
        text (str): Input string to be converted
        acronyms (optional, list of str): List of acronyms to honor

    Returns:
        str: Case converted text

    Examples:
        >>> pascal("hello world")
        'HelloWorld'
        >>> pascal("HELLO_HTML_WORLD", ["HTML"])
        'HelloHTMLWorld'
    """
    words, _case, _sep = parse_case(text, acronyms)
    return "".join(words)


def snake(text: str, acronyms: Optional[List[str]] = None) -> str:
    """Return text in snake_case style.

    Args:
        text (str): Input string to be converted
        acronyms (optional, list of str): List of acronyms to honort

    Returns:
        str: Case converted text

    Examples:
        >>> snake("hello world")
        'hello_world'
        >>> snake("HelloHTMLWorld", ["HTML"])
        'hello_html_world'
    """
    words, _case, _sep = parse_case(text, acronyms)
    return "_".join([w.lower() for w in words])


def dash(text: str, acronyms: Optional[List[str]] = None) -> str:
    """Return text in dash-case style.

    This case style is also known as: kebab-case, spinal-case, slug-case

    Args:
        text (str): Input string to be converted
        acronyms (optional, list of str): List of acronyms to honor

    Returns:
        str: Case converted text

    Examples:
        >>> dash("hello world")
        'hello-world'
        >>> dash("HelloHTMLWorld", ["HTML"])
        'hello-html-world'
    """
    words, _case, _sep = parse_case(text, acronyms)
    return "-".join([w.lower() for w in words])


def const(text: str, acronyms: Optional[List[str]] = None) -> str:
    """Return text in CONST_CASE style.

    This case style is also known as: SCREAMING_SNAKE_CASE

    Args:
        text (str): Input string to be converted
        acronyms (optional, list of str): List of acronyms to honor

    Returns:
        str: Case converted text

    Examples:
        >>> const("hello world")
        'HELLO_WORLD'
        >>> const("helloHTMLWorld", ["HTML"])
        'HELLO_HTML_WORLD'
    """
    words, _case, _sep = parse_case(text, acronyms)
    return "_".join([w.upper() for w in words])


def dot(text: str, acronyms: Optional[List[str]] = None) -> str:
    """Return text in dot.case style.

    Args:
        text (str): Input string to be converted
        acronyms (optional, list of str): List of acronyms to honor

    Returns:
        str: Case converted text

    Examples:
        >>> dot("hello world")
        'hello.world'
        >>> dot("helloHTMLWorld", ["HTML"])
        'hello.html.world'
    """
    words, _case, _sep = parse_case(text, acronyms)
    return ".".join([w.lower() for w in words])


def separate_words(text: str, acronyms: Optional[List[str]] = None) -> str:
    """Return text in "seperate words" style.

    Args:
        text (str): Input string to be converted
        acronyms (optional, list of str): List of acronyms to honor

    Returns:
        str: Case converted text

    Examples:
        >>> separate_words("HELLO_WORLD")
        'HELLO WORLD'
        >>> separate_words("helloHTMLWorld", ["HTML"])
        'hello HTML World'
    """
    words, _case, _sep = parse_case(text, acronyms, preserve_case=True)
    return " ".join(words)


def slash(text: str, acronyms: Optional[List[str]] = None) -> str:
    """Return text in slash/case style.

    Args:
        text (str): Input string to be converted
        acronyms (optional, list of str): List of acronyms to honor

    Returns:
        str: Case converted text

    Examples:
        >>> slash("HELLO_WORLD")
        'HELLO/WORLD'
        >>> slash("helloHTMLWorld", ["HTML"])
        'hello/HTML/World'
    """
    words, _case, _sep = parse_case(text, acronyms, preserve_case=True)
    return "/".join(words)


def backslash(text: str, acronyms: Optional[List[str]] = None) -> str:
    r"""Return text in backslash\case style.

    Args:
        text (str): Input string to be converted
        acronyms (optional, list of str): List of acronyms to honor

    Returns:
        str: Case converted text

    Examples:
        >>> backslash("HELLO_WORLD")
        r'HELLO\WORLD'
        >>> backslash("helloHTMLWorld", ["HTML"])
        r'hello\HTML\World'
    """
    words, _case, _sep = parse_case(text, acronyms, preserve_case=True)
    return "\\".join(words)


def ada(text: str, acronyms: Optional[List[str]] = None) -> str:
    """Return text in Ada_Case style.

    This case style is also known as: Camel_Snake

    Args:
        text (str): Input string to be converted
        acronyms (optional, list of str): List of acronyms to honor

    Returns:
        str: Case converted text

    Examples:
        >>> ada("hello_world")
        Hello_World
        >>> ada("helloHTMLWorld", ["HTML"])
        Hello_HTML_World
    """
    words, _case, _sep = parse_case(text, acronyms)
    return "_".join([w.capitalize() for w in words])


def title(text: str, acronyms: Optional[List[str]] = None) -> str:
    """Return text in Title_case style.

    Args:
        text (str): Input string to be converted
        acronyms (optional, list of str): List of acronyms to honor

    Returns:
        str: Case converted text

    Examples:
        >>> title("hello_world")
        Hello_world
        >>> title("helloHTMLWorld", ["HTML"])
        Hello_HTML_world
    """
    return cls.snake(text, acronyms).capitalize()


def lower(text: str, acronyms: Optional[List[str]] = None) -> str:
    """Return text in lowercase style.

    Args:
        text (str): Input string to be converted
        acronyms (optional, list of str): List of acronyms to honor

    Returns:
        str: Case converted text

    Examples:
        >>> lower("HELLO_WORLD")
        hello_world
        >>> lower("helloHTMLWorld", ["HTML"])
        Hello_HTML_world
    """
    return text.lower()


def upper(text: str, acronyms: Optional[List[str]] = None) -> str:
    """Return text in UPPERCASE style.

    Args:
        text (str): Input string to be converted
        acronyms (optional, list of str): List of acronyms to honor

    Returns:
        str: Case converted text

    Examples:
        >>> upper("hello_world")
        HELLO_WORLD
        >>> upper("helloHTMLWorld", ["HTML"])
        Hello_HTML_world
    """
    return text.upper()


def capital(text: str, acronyms: Optional[List[str]] = None) -> str:
    """Return text in UPPERCASE style.

    Args:
        text (str): Input string to be converted
        acronyms (optional, list of str): List of acronyms to honor

    Returns:
        str: Case converted text

    Examples:
        >>> capital("hello_world")
        HELLO_WORLD
        >>> capital("helloHTMLWorld", ["HTML"])
        Hello_HTML_world
    """
    return text.capitalize()


def http_header(text: str, acronyms: Optional[List[str]] = None) -> str:
    """Return text in Http-Header-Case style.

    Args:
        text (str): Input string to be converted
        acronyms (optional, list of str): List of acronyms to honor

    Returns:
        str: Case converted text

    Examples:
        >>> http_header("hello_world")
        Hello-World
        >>> http_header("helloHTMLWorld", ["HTML"])
        Hello-HTML-World
    """
    words, _case, _sep = parse_case(text, acronyms)
    return "-".join([w.capitalize() for w in words])
