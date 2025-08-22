from .parser import ParseData, Word, parse_case


####### CLASS STYLE #######
class Converter:
    parse_data: ParseData | None
    acronyms: list[str]

    def __init__(self, text: str | None = None, acronyms: list[str] | None = None):
        if text:
            self.parse_data = parse_case(text, acronyms)
        else:
            self.parse_data = None
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
            return Converter(text=text, acronyms=self.acronyms).camel()
        elif self.parse_data:
            words = self.parse_data.words
            if not words:
                return ""
            camel_words = [word.normalized_word for word in words]
            camel_words[0] = camel_words[0].lower()
            return "".join(camel_words)

        return ""

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
            return Converter(text=text, acronyms=self.acronyms).pascal()
        elif self.parse_data:
            words = self.parse_data.words
            return "".join([word.normalized_word for word in words])

        return ""

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
            return Converter(text=text, acronyms=self.acronyms).snake()
        elif self.parse_data:
            words = self.parse_data.words
            return "_".join([word.normalized_word.lower() for word in words])

        return ""

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
            return Converter(text=text, acronyms=self.acronyms).dash()
        elif self.parse_data:
            words = self.parse_data.words
            return "-".join([word.normalized_word.lower() for word in words])

        return ""

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
            return Converter(text=text, acronyms=self.acronyms).const()
        elif self.parse_data:
            words = self.parse_data.words
            return "_".join([word.normalized_word.upper() for word in words])

        return ""

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
            return Converter(text=text, acronyms=self.acronyms).dot()
        elif self.parse_data:
            words = self.parse_data.words
            return ".".join([word.normalized_word.lower() for word in words])

        return ""

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
            'hello HTML World'
            >>> converter.separate_words("A_DIFFERENT_HTML_STRING")
            'a different html string'
        """
        if text:
            return Converter(text=text, acronyms=self.acronyms).separate_words()
        elif self.parse_data:
            words = self.parse_data.words
            return " ".join([word.original_word for word in words])

        return ""

    def slash(self, text: str | None = None) -> str:
        """Return text in "slash/string" style.

        Args:
            text (str): Input string to be converted
            acronyms (optional, list of str): List of acronyms to honor

        Returns:
            str: Case converted text

        Examples:
            >>> converter = Converter("hello world")
            >>> converter.slash("hello world")
            'hello/world'
            >>> converter = Converter(text="helloHTMLWorld", acronyms=["HTML"])
            >>> converter.slash()
            'hello/HTML/World'
            >>> converter.separate_words("A_DIFFERENT_HTML_STRING")
            'A/DIFFERENT/HTML/STRING'
        """
        if text:
            return Converter(text=text, acronyms=self.acronyms).slash()
        elif self.parse_data:
            words = self.parse_data.words
            return "/".join([word.original_word for word in words])

        return ""

    def backslash(self, text: str | None = None) -> str:
        """Return text in "backslash\\string" style.

        Args:
            text (str): Input string to be converted
            acronyms (optional, list of str): List of acronyms to honor

        Returns:
            str: Case converted text

        Examples:
            >>> converter = Converter("hello world")
            >>> converter.backslash("hello world")
            'hello\\world'
            >>> converter = Converter(text="helloHTMLWorld", acronyms=["HTML"])
            >>> converter.backslash()
            'hello\\HTML\\World'
            >>> converter.separate_words("A_DIFFERENT_HTML_STRING")
            'A\\DIFFERENT\\HTML\\STRING'
        """
        if text:
            return Converter(text=text, acronyms=self.acronyms).backslash()
        elif self.parse_data:
            words = self.parse_data.words
            return "\\".join([word.original_word for word in words])

        return ""


######### CONVENIENCE FUNCTION STYLE #############
def camel(text: str, acronyms: list[str] | None = None) -> str:
    """Return text in camelCase style.

    Convenience function for Converter(text, acronyms).camel()

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
    return Converter(text=text, acronyms=acronyms).camel()


def pascal(text: str, acronyms: list[str] | None = None) -> str:
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
    return Converter(text=text, acronyms=acronyms).pascal()


def snake(text: str, acronyms: list[str] | None = None) -> str:
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
    return Converter(text=text, acronyms=acronyms).snake()


def dash(text: str, acronyms: list[str] | None = None) -> str:
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
    return Converter(text=text, acronyms=acronyms).dash()


def const(text: str, acronyms: list[str] | None = None) -> str:
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
    return Converter(text=text, acronyms=acronyms).const()


def dot(text: str, acronyms: list[str] | None = None) -> str:
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
    return Converter(text=text, acronyms=acronyms).dot()


def separate_words(text: str, acronyms: list[str] | None = None) -> str:
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
    return Converter(text=text, acronyms=acronyms).separate_words()


def slash(text: str, acronyms: list[str] | None = None) -> str:
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
    return Converter(text=text, acronyms=acronyms).slash()


def backslash(text: str, acronyms: list[str] | None = None) -> str:
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
    return Converter(text=text, acronyms=acronyms).backslash()


def ada(text: str, acronyms: list[str] | None = None) -> str:
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
    parse_data = parse_case(text, acronyms)
    return "_".join([w.normalized_word for w in parse_data.words])


def http_header(text: str, acronyms: list[str] | None = None) -> str:
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
    parse_data = parse_case(text, acronyms)
    return "-".join([w.normalized_word for w in parse_data.words])


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
        hello_html_world
    """
    # TODO: add docstring tests
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
        HELLOHTMLWORLD
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
        HelloHTMLWorld
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
        Hello_world
        >>> capital("helloHTMLWorld", ["HTML"])
        HelloHTMLWorld
    """
    return text.capitalize()
