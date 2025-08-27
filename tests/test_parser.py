import pytest

from case_conversion import parse_into_words
from case_conversion.parser import ParsedWord, segment_string


@pytest.mark.parametrize(
    "string,acronyms,expected",
    [
        (
            "fooBarBaz",
            None,
            [
                ParsedWord(original_word="foo", normalized_word="Foo"),
                ParsedWord(original_word="Bar", normalized_word="Bar"),
                ParsedWord(original_word="Baz", normalized_word="Baz"),
            ],
        ),
        (
            "fooBarBaz",
            ["BAR"],
            [
                ParsedWord(original_word="foo", normalized_word="Foo"),
                ParsedWord(original_word="Bar", normalized_word="BAR"),
                ParsedWord(original_word="Baz", normalized_word="Baz"),
            ],
        ),
    ],
)
def test_parse_case(string, acronyms, expected):
    assert parse_into_words(string, acronyms) == expected


@pytest.mark.parametrize(
    "string,expected",
    (
        ("fooBarString", ["foo", "Bar", "String"]),
        ("FooBarString", ["Foo", "Bar", "String"]),
        ("foo_bar_string", ["foo", None, "bar", None, "string"]),
        ("foo-bar-string", ["foo", None, "bar", None, "string"]),
        ("FOO_BAR_STRING", ["FOO", None, "BAR", None, "STRING"]),
        ("foo.bar.string", ["foo", None, "bar", None, "string"]),
        ("foo bar string", ["foo", None, "bar", None, "string"]),
        ("foo/bar/string", ["foo", None, "bar", None, "string"]),
        ("foo\\bar\\string", ["foo", None, "bar", None, "string"]),
        ("foobarstring", ["foobarstring"]),
        ("FOOBARSTRING", ["FOOBARSTRING"]),
    ),
)
def test_segment_string(string, expected):
    assert segment_string(string) == expected
