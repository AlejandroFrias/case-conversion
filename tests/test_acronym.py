import pytest

from case_conversion.acronym import (
    InvalidAcronymError,
    advanced_acronym_detection,
    normalize_acronyms,
    simple_acronym_detection,
)
from case_conversion.converter import snake


@pytest.mark.parametrize(
    "acronyms,expected",
    (
        (("http",), ["HTTP"]),
        (
            ("HTTP",),
            ["HTTP"],
        ),
        (
            ("Http",),
            ["HTTP"],
        ),
        (
            ("httP",),
            ["HTTP"],
        ),
        (("http", "Nasa"), ["HTTP", "NASA"]),
    ),
)
def test_sanitize_acronyms(acronyms, expected):
    assert normalize_acronyms(acronyms) == expected


def test_sanitize_acronyms_invalid():
    with pytest.raises(InvalidAcronymError):
        normalize_acronyms(["HTTP", ""])


@pytest.mark.parametrize(
    "s,i,words,expected",
    (
        (0, 1, ["FOO", "bar"], 0),
        (1, 2, ["foo", "BAR", "baz"], 1),
    ),
)
def test_simple_acronym_detection(s, i, words, expected):
    assert simple_acronym_detection(s, i, words) == expected


@pytest.mark.parametrize(
    "s,i,words,acronyms,expected",
    (
        (0, 1, ["FOO", "bar"], ("FOO",), 0),
        (0, 1, ["FOO", "bar"], ("BAR",), 0),
        (0, 1, ["FOFOO"], ("FOO", "FO"), 1),
    ),
)
def test_advanced_acronym_detection(s, i, words, acronyms, expected):
    assert advanced_acronym_detection(s, i, words, acronyms) == expected


def test_advanced_acronym_detection_with_fallback_to_simple():
    assert snake("fooBARBAZError", acronyms=["BAR"]) == "foo_bar_baz_error"
    assert snake("fooBARBAZError", acronyms=["BAZ"]) == "foo_bar_baz_error"
    assert snake("fooBARBAZBAR", acronyms=["BAZ"]) == "foo_bar_baz_bar"
    assert snake("BARBAZBAR", acronyms=["BAZ"]) == "bar_baz_bar"


@pytest.mark.parametrize("acronyms", ("HT-TP", "NA SA", "SU.GAR"))
def test_sanitize_acronyms_raises_on_invalid_acronyms(acronyms):
    with pytest.raises(InvalidAcronymError):
        normalize_acronyms(acronyms)
