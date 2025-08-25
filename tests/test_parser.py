import pytest

from case_conversion import parse_case
from case_conversion.parser import ParseData, Word


@pytest.mark.parametrize(
    "string,acronyms,expected",
    (
        (
            "fooBarBaz",
            None,
            ParseData(
                words=[
                    Word(original_word="foo", normalized_word="Foo"),
                    Word(original_word="Bar", normalized_word="Bar"),
                    Word(original_word="Baz", normalized_word="Baz"),
                ],
                original_separator="",
            ),
        ),
        (
            "fooBarBaz",
            ["BAR"],
            ParseData(
                words=[
                    Word(original_word="foo", normalized_word="Foo"),
                    Word(original_word="Bar", normalized_word="BAR"),
                    Word(original_word="Baz", normalized_word="Baz"),
                ],
                original_separator="",
            ),
        ),
    ),
)
def test_parse_case(string, acronyms, expected):
    assert parse_case(string, acronyms) == expected
