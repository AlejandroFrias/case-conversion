from typing import List, Optional

from case_conversion.types import Case

from .parser import parse_case


####### CLASS STYLE #######
class Converter:
    case: Case | None
    text: str | None
    words: list[str] | None
    separators: str | None
    acronyms: list[str]

    def __init__(self, text: str | None = None, acronyms: list[str] | None = None):
        if text:
            words, case, separators = parse_case(text, acronyms)
            self.text = text
            self.words = words
            self.separators = separators
            self.case = case
        else:
            self.words = None
        self.acronyms = acronyms or []

    def camel(self, text: str | None = None) -> str:
        """Return text in camelCase style.

        Args:
            text (str): Input string to be converted
            acronyms (optional, list of str): List of acronyms to honor

        Returns:
            str: Case converted text

        Examples:
            >>> converter = Converter(text="hello world")
            >>> converter.camel()
            'helloWorld'
            >>> converter = Converter(acronyms=["HTML"])
            >>> converter.camel("HELLO_HTML_WORLD)
            'helloHTMLWorld'
        """
        if text:
            words, *_ = parse_case(text, self.acronyms)
            return _camel(words)
        return _camel(self.words or [])

    def pascal(self, text: str | None = None) -> str:
        """Return text in PascalCase style.

        This case style is also known as: MixedCase

        Args:
            text (str): Input string to be converted
            acronyms (optional, list of str): List of acronyms to honor

        Returns:
            str: Case converted text

        Examples:
            >>> converter = Converter(text="hello world")
            >>> converter.pascal()
            'HelloWorld'
            >>> converter = Converter(text="hello_html_world", acronyms=["HTML"])
            >>> converter.pascal()
            'HelloHTMLWorld'
            >>> converter.pascal("A_DIFFERENT_HTML_STRING")
            'ADifferentHTMLString'
        """
        if text:
            words, *_ = parse_case(text, self.acronyms)
            return _pascal(words)
        return _pascal(self.words or [])

    def snake(self, text: str | None = None) -> str:
        """Return text in snake_case style.

        Args:
            text (str): Input string to be converted
            acronyms (optional, list of str): List of acronyms to honor

        Returns:
            str: Case converted text

        Examples:
            >>> converter = Converter("hello world")
            >>> converter.snake("hello world")
            'hello_world'
            >>> converter = Converter(text="helloHTMLWorld", acronyms=["HTML"])
            >>> converter.snake()
            'hello_html_world'
            >>> converter.snake("A_DIFFERENT_HTML_STRING")
            'a_different_html_string'
        """
        if text:
            words, *_ = parse_case(text, self.acronyms)
            return _snake(words)
        return _snake(self.words or [])

    def dash(self, text: str | None = None) -> str:
        """Return text in dash-case style.

        Args:
            text (str): Input string to be converted
            acronyms (optional, list of str): List of acronyms to honor

        Returns:
            str: Case converted text

        Examples:
            >>> converter = Converter("hello world")
            >>> converter.dash("hello world")
            'hello-world'
            >>> converter = Converter(text="helloHTMLWorld", acronyms=["HTML"])
            >>> converter.dash()
            'hello-html-world'
            >>> converter.dash("A_DIFFERENT_HTML_STRING")
            'a-different-html-string'
        """
        if text:
            words, *_ = parse_case(text, self.acronyms)
            return _dash(words)
        return _dash(self.words or [])

    def const(self, text: str | None = None) -> str:
        """Return text in CONST_CASE style.

        This case style is also known as: SCREAMING_SNAKE_CASE

        Args:
            text (str): Input string to be converted
            acronyms (optional, list of str): List of acronyms to honor

        Returns:
            str: Case converted text

        Examples:
            >>> converter = Converter("hello world")
            >>> converter.const("hello world")
            'HELLO_WORLD'
            >>> converter = Converter(text="helloHTMLWorld", acronyms=["HTML"])
            >>> converter.const()
            'HELLO_HTML_WORLD'
            >>> converter.const("A_DIFFERENT_HTML_STRING")
            'A_DIFFERENT_HTML_STRING'
        """
        if text:
            words, *_ = parse_case(text, self.acronyms)
            return _const(words)
        return _const(self.words or [])

    def dot(self, text: str | None = None) -> str:
        """Return text in dot.case style.

        Args:
            text (str): Input string to be converted
            acronyms (optional, list of str): List of acronyms to honor

        Returns:
            str: Case converted text

        Examples:
            >>> converter = Converter("hello world")
            >>> converter.dot("hello world")
            'hello.world'
            >>> converter = Converter(text="helloHTMLWorld", acronyms=["HTML"])
            >>> converter.dot()
            'hello.html.world'
            >>> converter.dot("A_DIFFERENT_HTML_STRING")
            'a.different.html.string'
        """
        if text:
            words, *_ = parse_case(text, self.acronyms)
            return _dot(words)
        return _dot(self.words or [])

    def separate_words(self, text: str | None = None) -> str:
        """Return text in "separate words" style.

        Args:
            text (str): Input string to be converted
            acronyms (optional, list of str): List of acronyms to honor

        Returns:
            str: Case converted text

        Examples:
            >>> converter = Converter("hello world")
            >>> converter.separate_words("hello world")
            'hello world'
            >>> converter = Converter(text="helloHTMLWorld", acronyms=["HTML"])
            >>> converter.separate_words()
            'hello world'
            >>> converter.separate_words("A_DIFFERENT_HTML_STRING")
            'a different html string'
        """
        if text:
            words, *_ = parse_case(text, self.acronyms)
            return _separate_words(words)
        return _separate_words(self.words or [])


############# HELPERS: word list -> str #################


def _camel(words: list[str]) -> str:
    if not words:
        return ""
    words[0] = words[0].lower()
    return "".join(words)


def _pascal(words: list[str]) -> str:
    return "".join(words)


def _snake(words: list[str]) -> str:
    return "_".join([w.lower() for w in words])


def _dash(words: list[str]) -> str:
    return "-".join([w.lower() for w in words])


def _dot(words: list[str]) -> str:
    return ".".join([w.lower() for w in words])


def _const(words: list[str]) -> str:
    return "_".join([w.upper() for w in words])


def _separate_words(words: List[str]) -> str:
    return " ".join(words)


######### FUNCTION STYLE #############
def camel(text: str, acronyms: list[str] | None = None) -> str:
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
    words, *_ = parse_case(text, acronyms)
    return _camel(words)


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
    words, *_ = parse_case(text, acronyms)
    return _pascal(words)


def snake(text: str, acronyms: Optional[List[str]] = None) -> str:
    """Return text in snake_case style.

    Args:
        text (str): Input string to be converted
        acronyms (optional, list of str): List of acronyms to honor

    Returns:
        str: Case converted text

    Examples:
        >>> snake("hello world")
        'hello_world'
        >>> snake("HelloHTMLWorld", ["HTML"])
        'hello_html_world'
    """
    words, *_ = parse_case(text, acronyms)
    return _snake(words)


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
    words, *_ = parse_case(text, acronyms)
    return _dash(words)


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
    words, *_ = parse_case(text, acronyms)
    return _const(words)


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
    words, *_ = parse_case(text, acronyms)
    return _dot(words)


def separate_words(text: str, acronyms: Optional[List[str]] = None) -> str:
    """Return text in "separate words" style.

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
    words, *_ = parse_case(text, acronyms, preserve_case=True)
    return _separate_words(words)


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
    words, *_ = parse_case(text, acronyms, preserve_case=True)
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
    words, *_ = parse_case(text, acronyms, preserve_case=True)
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
    words, *_ = parse_case(text, acronyms)
    return "_".join([w.capitalize() for w in words])


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
    words, *_ = parse_case(text, acronyms)
    return "-".join([w.capitalize() for w in words])


def lower(text: str, *args, **kwargs) -> str:
    """Return text in lowercase style.

    This is a convenience function wrapping inbuilt lower().
    It features the same signature as other conversion functions.
    Note: Acronyms are not being honored.

    Args:
        text (str): Input string to be converted
        args : Placeholder to conform to common signature
        kwargs : Placeholder to conform to common signature

    Returns:
        str: Case converted text

    Examples:
        >>> lower("HELLO_WORLD")
        hello_world
        >>> lower("helloHTMLWorld", ["HTML"])
        Hello_HTML_world
    """
    return text.lower()


def upper(text: str, *args, **kwargs) -> str:
    """Return text in UPPERCASE style.

    This is a convenience function wrapping inbuilt upper().
    It features the same signature as other conversion functions.
    Note: Acronyms are not being honored.

    Args:
        text (str): Input string to be converted
        args : Placeholder to conform to common signature
        kwargs : Placeholder to conform to common signature

    Returns:
        str: Case converted text

    Examples:
        >>> upper("hello_world")
        HELLO_WORLD
        >>> upper("helloHTMLWorld", ["HTML"])
        Hello_HTML_world
    """
    return text.upper()


def title(text: str, *args, **kwargs) -> str:
    """Return text in Title_case style.

    This is a convenience function wrapping inbuilt title().
    It features the same signature as other conversion functions.
    Note: Acronyms are not being honored.

    Args:
        text (str): Input string to be converted
        args : Placeholder to conform to common signature
        kwargs : Placeholder to conform to common signature

    Returns:
        str: Case converted text

    Examples:
        >>> title("hello_world")
        Hello_world
        >>> title("helloHTMLWorld", ["HTML"])
        Hello_HTML_world
    """
    return text.title()


def capital(text: str, *args, **kwargs) -> str:
    """Return text in Capital case style.

    This is a convenience function wrapping inbuilt capitalize().
    It features the same signature as other conversion functions.
    Note: Acronyms are not being honored.

    Args:
        text (str): Input string to be converted
        args : Placeholder to conform to common signature
        kwargs : Placeholder to conform to common signature

    Returns:
        str: Case converted text

    Examples:
        >>> capital("hello_world")
        HELLO_WORLD
        >>> capital("helloHTMLWorld", ["HTML"])
        Hello_HTML_world
    """
    return text.capitalize()
