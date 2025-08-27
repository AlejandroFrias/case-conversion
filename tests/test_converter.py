from unittest import TestCase

from parameterized import parameterized

import case_conversion

ACRONYMS = ["HTTP"]
ACRONYMS_UNICODE = ["HÉÉP"]

# These cases do not preserve capitals from the original string
CASES = [
    "camel",
    "pascal",
    "mixed",
    "snake",
    "dash",
    "kebab",
    "spinal",
    "slug",
    "const",
    "screaming_snake",
    "dot",
    "ada",
    "http_header",
]

# These cases preserve the capitals from the original string
CASES_PRESERVE = ["separate_words", "slash", "backslash"]

VALUES = {
    "camel": "fooBarString",
    "pascal": "FooBarString",
    "mixed": "FooBarString",
    "snake": "foo_bar_string",
    "dash": "foo-bar-string",
    "kebab": "foo-bar-string",
    "spinal": "foo-bar-string",
    "slug": "foo-bar-string",
    "const": "FOO_BAR_STRING",
    "screaming_snake": "FOO_BAR_STRING",
    "dot": "foo.bar.string",
    "separate_words": "foo bar string",
    "slash": "foo/bar/string",
    "backslash": "foo\\bar\\string",
    "ada": "Foo_Bar_String",
    "http_header": "Foo-Bar-String",
}

VALUES_UNICODE = {
    "camel": "fóoBarString",
    "pascal": "FóoBarString",
    "mixed": "FóoBarString",
    "snake": "fóo_bar_string",
    "dash": "fóo-bar-string",
    "kebab": "fóo-bar-string",
    "spinal": "fóo-bar-string",
    "slug": "fóo-bar-string",
    "const": "FÓO_BAR_STRING",
    "screaming_snake": "FÓO_BAR_STRING",
    "dot": "fóo.bar.string",
    "separate_words": "fóo bar string",
    "slash": "fóo/bar/string",
    "backslash": "fóo\\bar\\string",
    "ada": "Fóo_Bar_String",
    "http_header": "Fóo-Bar-String",
}

VALUES_SINGLE = {
    "camel": "foo",
    "pascal": "Foo",
    "mixed": "Foo",
    "snake": "foo",
    "dash": "foo",
    "kebab": "foo",
    "spinal": "foo",
    "slug": "foo",
    "const": "FOO",
    "screaming_snake": "FOO",
    "dot": "foo",
    "separate_words": "foo",
    "slash": "foo",
    "backslash": "foo",
    "ada": "Foo",
    "http_header": "Foo",
}

VALUES_SINGLE_UNICODE = {
    "camel": "fóo",
    "pascal": "Fóo",
    "mixed": "Fóo",
    "snake": "fóo",
    "dash": "fóo",
    "kebab": "fóo",
    "spinal": "fóo",
    "slug": "fóo",
    "const": "FÓO",
    "screaming_snake": "FÓO",
    "dot": "fóo",
    "separate_words": "fóo",
    "slash": "fóo",
    "backslash": "fóo",
    "ada": "Fóo",
    "http_header": "Fóo",
}

VALUES_ACRONYM = {
    "camel": "fooHTTPBarString",
    "pascal": "FooHTTPBarString",
    "mixed": "FooHTTPBarString",
    "snake": "foo_http_bar_string",
    "dash": "foo-http-bar-string",
    "kebab": "foo-http-bar-string",
    "spinal": "foo-http-bar-string",
    "slug": "foo-http-bar-string",
    "const": "FOO_HTTP_BAR_STRING",
    "screaming_snake": "FOO_HTTP_BAR_STRING",
    "dot": "foo.http.bar.string",
    "separate_words": "foo http bar string",
    "slash": "foo/http/bar/string",
    "backslash": "foo\\http\\bar\\string",
    "ada": "Foo_HTTP_Bar_String",
    "http_header": "Foo-HTTP-Bar-String",
}

VALUES_ACRONYM_UNICODE = {
    "camel": "fooHÉÉPBarString",
    "pascal": "FooHÉÉPBarString",
    "mixed": "FooHÉÉPBarString",
    "snake": "foo_héép_bar_string",
    "dash": "foo-héép-bar-string",
    "kebab": "foo-héép-bar-string",
    "spinal": "foo-héép-bar-string",
    "slug": "foo-héép-bar-string",
    "const": "FOO_HÉÉP_BAR_STRING",
    "screaming_snake": "FOO_HÉÉP_BAR_STRING",
    "dot": "foo.héép.bar.string",
    "separate_words": "foo héép bar string",
    "slash": "foo/héép/bar/string",
    "backslash": "foo\\héép\\bar\\string",
    "ada": "Foo_HÉÉP_Bar_String",
    "http_header": "Foo-HÉÉP-Bar-String",
}

PRESERVE_VALUES = {
    "separate_words": {
        "camel": "foo Bar String",
        "pascal": "Foo Bar String",
        "mixed": "Foo Bar String",
        "const": "FOO BAR STRING",
        "screaming_snake": "FOO BAR STRING",
        "ada": "Foo Bar String",
        "http_header": "Foo Bar String",
        "default": "foo bar string",
    },
    "slash": {
        "camel": "foo/Bar/String",
        "pascal": "Foo/Bar/String",
        "mixed": "Foo/Bar/String",
        "const": "FOO/BAR/STRING",
        "screaming_snake": "FOO/BAR/STRING",
        "ada": "Foo/Bar/String",
        "http_header": "Foo/Bar/String",
        "default": "foo/bar/string",
    },
    "backslash": {
        "camel": "foo\\Bar\\String",
        "pascal": "Foo\\Bar\\String",
        "mixed": "Foo\\Bar\\String",
        "const": "FOO\\BAR\\STRING",
        "screaming_snake": "FOO\\BAR\\STRING",
        "ada": "Foo\\Bar\\String",
        "http_header": "Foo\\Bar\\String",
        "default": "foo\\bar\\string",
    },
}

PRESERVE_VALUES_UNICODE = {
    "separate_words": {
        "camel": "fóo Bar String",
        "pascal": "Fóo Bar String",
        "mixed": "Fóo Bar String",
        "const": "FÓO BAR STRING",
        "screaming_snake": "FÓO BAR STRING",
        "ada": "Fóo Bar String",
        "http_header": "Fóo Bar String",
        "default": "fóo bar string",
    },
    "slash": {
        "camel": "fóo/Bar/String",
        "pascal": "Fóo/Bar/String",
        "mixed": "Fóo/Bar/String",
        "const": "FÓO/BAR/STRING",
        "screaming_snake": "FÓO/BAR/STRING",
        "ada": "Fóo/Bar/String",
        "http_header": "Fóo/Bar/String",
        "default": "fóo/bar/string",
    },
    "backslash": {
        "camel": "fóo\\Bar\\String",
        "pascal": "Fóo\\Bar\\String",
        "mixed": "Fóo\\Bar\\String",
        "const": "FÓO\\BAR\\STRING",
        "screaming_snake": "FÓO\\BAR\\STRING",
        "ada": "Fóo\\Bar\\String",
        "http_header": "Fóo\\Bar\\String",
        "default": "fóo\\bar\\string",
    },
}

PRESERVE_VALUES_SINGLE = {
    "separate_words": {
        "camel": "foo",
        "pascal": "Foo",
        "mixed": "Foo",
        "const": "FOO",
        "screaming_snake": "FOO",
        "ada": "Foo",
        "http_header": "Foo",
        "default": "foo",
    },
    "slash": {
        "camel": "foo",
        "pascal": "Foo",
        "mixed": "Foo",
        "const": "FOO",
        "screaming_snake": "FOO",
        "ada": "Foo",
        "http_header": "Foo",
        "default": "foo",
    },
    "backslash": {
        "camel": "foo",
        "pascal": "Foo",
        "mixed": "Foo",
        "const": "FOO",
        "screaming_snake": "FOO",
        "ada": "Foo",
        "http_header": "Foo",
        "default": "foo",
    },
}

PRESERVE_VALUES_SINGLE_UNICODE = {
    "separate_words": {
        "camel": "fóo",
        "pascal": "Fóo",
        "mixed": "Fóo",
        "const": "FÓO",
        "screaming_snake": "FÓO",
        "ada": "Fóo",
        "http_header": "Fóo",
        "default": "fóo",
    },
    "slash": {
        "camel": "fóo",
        "pascal": "Fóo",
        "mixed": "Fóo",
        "const": "FÓO",
        "screaming_snake": "FÓO",
        "ada": "Fóo",
        "http_header": "Fóo",
        "default": "fóo",
    },
    "backslash": {
        "camel": "fóo",
        "pascal": "Fóo",
        "mixed": "Fóo",
        "const": "FÓO",
        "screaming_snake": "FÓO",
        "ada": "Fóo",
        "http_header": "Fóo",
        "default": "fóo",
    },
}

PRESERVE_VALUES_ACRONYM = {
    "separate_words": {
        "camel": "foo HTTP Bar String",
        "pascal": "Foo HTTP Bar String",
        "mixed": "Foo HTTP Bar String",
        "const": "FOO HTTP BAR STRING",
        "screaming_snake": "FOO HTTP BAR STRING",
        "ada": "Foo HTTP Bar String",
        "http_header": "Foo HTTP Bar String",
        "default": "foo http bar string",
    },
    "slash": {
        "camel": "foo/HTTP/Bar/String",
        "pascal": "Foo/HTTP/Bar/String",
        "mixed": "Foo/HTTP/Bar/String",
        "const": "FOO/HTTP/BAR/STRING",
        "screaming_snake": "FOO/HTTP/BAR/STRING",
        "ada": "Foo/HTTP/Bar/String",
        "http_header": "Foo/HTTP/Bar/String",
        "default": "foo/http/bar/string",
    },
    "backslash": {
        "camel": "foo\\HTTP\\Bar\\String",
        "pascal": "Foo\\HTTP\\Bar\\String",
        "mixed": "Foo\\HTTP\\Bar\\String",
        "const": "FOO\\HTTP\\BAR\\STRING",
        "screaming_snake": "FOO\\HTTP\\BAR\\STRING",
        "ada": "Foo\\HTTP\\Bar\\String",
        "http_header": "Foo\\HTTP\\Bar\\String",
        "default": "foo\\http\\bar\\string",
    },
}

PRESERVE_VALUES_ACRONYM_UNICODE = {
    "separate_words": {
        "camel": "foo HÉÉP Bar String",
        "pascal": "Foo HÉÉP Bar String",
        "mixed": "Foo HÉÉP Bar String",
        "const": "FOO HÉÉP BAR STRING",
        "screaming_snake": "FOO HÉÉP BAR STRING",
        "ada": "Foo HÉÉP Bar String",
        "http_header": "Foo HÉÉP Bar String",
        "default": "foo héép bar string",
    },
    "slash": {
        "camel": "foo/HÉÉP/Bar/String",
        "pascal": "Foo/HÉÉP/Bar/String",
        "mixed": "Foo/HÉÉP/Bar/String",
        "const": "FOO/HÉÉP/BAR/STRING",
        "screaming_snake": "FOO/HÉÉP/BAR/STRING",
        "ada": "Foo/HÉÉP/Bar/String",
        "http_header": "Foo/HÉÉP/Bar/String",
        "default": "foo/héép/bar/string",
    },
    "backslash": {
        "camel": "foo\\HÉÉP\\Bar\\String",
        "pascal": "Foo\\HÉÉP\\Bar\\String",
        "mixed": "Foo\\HÉÉP\\Bar\\String",
        "const": "FOO\\HÉÉP\\BAR\\STRING",
        "screaming_snake": "FOO\\HÉÉP\\BAR\\STRING",
        "ada": "Foo\\HÉÉP\\Bar\\String",
        "http_header": "Foo\\HÉÉP\\Bar\\String",
        "default": "foo\\héép\\bar\\string",
    },
}


PRESERVE_VALUES_ACRONYM_SINGLE = {
    "separate_words": {
        "camel": "HTTP",
        "pascal": "HTTP",
        "mixed": "HTTP",
        "const": "HTTP",
        "screaming_snake": "HTTP",
        "ada": "HTTP",
        "http_header": "HTTP",
        "default": "http",
    },
    "slash": {
        "camel": "HTTP",
        "pascal": "HTTP",
        "mixed": "HTTP",
        "const": "HTTP",
        "screaming_snake": "HTTP",
        "ada": "HTTP",
        "http_header": "HTTP",
        "default": "http",
    },
    "backslash": {
        "camel": "HTTP",
        "pascal": "HTTP",
        "mixed": "HTTP",
        "const": "HTTP",
        "screaming_snake": "HTTP",
        "ada": "HTTP",
        "http_header": "HTTP",
        "default": "http",
    },
}

CAPITAL_CASES = [
    "camel",
    "pascal",
    "mixed",
    "const",
    "screaming_snake",
    "ada",
    "http_header",
]


def _expand_values(values):
    test_params = []
    for case in CASES:
        test_params.extend(
            [
                (name + "2" + case, case, value, values[case])
                for name, value in values.items()
            ]
        )
        test_params.append((case + "_empty", case, "", ""))
    return test_params


def _expand_values_preserve(preserve_values, values):
    test_params = []
    for case in CASES_PRESERVE:
        test_params.extend(
            [
                (
                    name + "2" + case,
                    case,
                    value,
                    preserve_values[case][name if name in CAPITAL_CASES else "default"],
                )
                for name, value in values.items()
            ]
        )
        test_params.append((case + "_empty", case, "", ""))
    return test_params


class CaseConversionTest(TestCase):
    def assertConverter(
        self, case: str, value: str, expected: str, acronyms: list[str] | None = None
    ):
        # test function style, e.g. snake("helloWorld") -> "hello_world"
        case_converter = getattr(case_conversion, case)
        self.assertEqual(case_converter(value, acronyms), expected)

        # test class style with init text, e.g. Converter("helloWorld").snake() -> "hello_world"
        converter = case_conversion.Converter(text=value, acronyms=acronyms)
        case_converter = getattr(converter, case)
        self.assertEqual(case_converter(), expected)

        # test class style without init text, e.g. Converter().snake("helloWorld") -> "hello_world"
        converter = case_conversion.Converter(acronyms=acronyms)
        case_converter = getattr(converter, case)
        self.assertEqual(case_converter(value), expected)

    @parameterized.expand(_expand_values(VALUES))
    def test(self, _, case, value, expected):
        """
        Test conversions from all cases to all cases that don't preserve
        capital/lower case letters.
        """
        self.assertConverter(case, value, expected)

    @parameterized.expand(_expand_values(VALUES_UNICODE))
    def test_unicode(self, _, case, value, expected):
        """
        Test conversions from all cases to all cases that don't preserve
        capital/lower case letters (with unicode characters).
        """
        self.assertConverter(case, value, expected)

    @parameterized.expand(_expand_values(VALUES_SINGLE))
    def test_single(self, _, case, value, expected):
        """
        Test conversions of single words from all cases to all cases that
        don't preserve capital/lower case letters.
        """
        self.assertConverter(case, value, expected)

    @parameterized.expand(_expand_values(VALUES_SINGLE_UNICODE))
    def test_single_unicode(self, _, case, value, expected):
        """
        Test conversions of single words from all cases to all cases that
        don't preserve capital/lower case letters (with unicode characters).
        """
        self.assertConverter(case, value, expected)

    @parameterized.expand(_expand_values_preserve(PRESERVE_VALUES, VALUES))
    def test_preserve_case(self, _, case, value, expected):
        """
        Test conversions from all cases to all cases that do preserve
        capital/lower case letters.
        """
        self.assertConverter(case, value, expected)

    @parameterized.expand(
        _expand_values_preserve(PRESERVE_VALUES_UNICODE, VALUES_UNICODE)
    )
    def test_preserve_case_unicode(self, _, case, value, expected):
        """
        Test conversions from all cases to all cases that do preserve
        capital/lower case letters (with unicode characters).
        """
        self.assertConverter(case, value, expected)

    @parameterized.expand(
        _expand_values_preserve(PRESERVE_VALUES_SINGLE, VALUES_SINGLE)
    )
    def test_preserve_case_single(self, _, case, value, expected):
        """
        Test conversions of single words from all cases to all cases that do
        preserve capital/lower case letters.
        """
        self.assertConverter(case, value, expected)

    @parameterized.expand(
        _expand_values_preserve(PRESERVE_VALUES_SINGLE_UNICODE, VALUES_SINGLE_UNICODE)
    )
    def test_preserve_case_single_unicode(self, _, case, value, expected):
        """
        Test conversions of single words from all cases to all cases that do
        preserve capital/lower case letters (with unicode characters).
        """
        self.assertConverter(case, value, expected)

    @parameterized.expand(_expand_values(VALUES_ACRONYM))
    def test_acronyms(self, _, case, value, expected):
        """
        Test conversions from all cases to all cases that don't preserve
        capital/lower case letters (with acronym detection).
        """
        self.assertConverter(case, value, expected, acronyms=ACRONYMS)

    @parameterized.expand(_expand_values(VALUES_ACRONYM_UNICODE))
    def test_acronyms_unicode(self, _, case, value, expected):
        """
        Test conversions from all cases to all cases that don't preserve
        capital/lower case letters (with acronym detection and unicode
        characters).
        """
        self.assertConverter(case, value, expected, acronyms=ACRONYMS_UNICODE)

    @parameterized.expand(
        _expand_values_preserve(PRESERVE_VALUES_ACRONYM, VALUES_ACRONYM)
    )
    def test_acronyms_preserve_case(self, _, case, value, expected):
        """
        Test conversions from all cases to all cases that do preserve
        capital/lower case letters (with acronym detection).
        """
        self.assertConverter(case, value, expected, acronyms=ACRONYMS)

    @parameterized.expand(
        _expand_values_preserve(PRESERVE_VALUES_ACRONYM_UNICODE, VALUES_ACRONYM_UNICODE)
    )
    def test_acronyms_preserve_case_unicode(self, _, case, value, expected):
        """
        Test conversions from all cases to all cases that do preserve
        capital/lower case letters (with acronym detection and unicode
        characters).
        """
        self.assertConverter(case, value, expected, acronyms=ACRONYMS_UNICODE)
