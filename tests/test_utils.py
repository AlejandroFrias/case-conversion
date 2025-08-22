import pytest

import case_conversion.utils as utils
from case_conversion import Case, InvalidAcronymError


@pytest.mark.parametrize(
    "string,expected",
    (
        ("fooBarString", (["foo", "Bar", "String"], "")),
        ("FooBarString", (["Foo", "Bar", "String"], "")),
        ("foo_bar_string", (["foo", None, "bar", None, "string"], "_")),
        ("foo-bar-string", (["foo", None, "bar", None, "string"], "-")),
        ("FOO_BAR_STRING", (["FOO", None, "BAR", None, "STRING"], "_")),
        ("foo.bar.string", (["foo", None, "bar", None, "string"], ".")),
        ("foo bar string", (["foo", None, "bar", None, "string"], " ")),
        ("foo/bar/string", (["foo", None, "bar", None, "string"], "/")),
        ("foo\\bar\\string", (["foo", None, "bar", None, "string"], "\\")),
        ("foobarstring", (["foobarstring"], "")),
        ("FOOBARSTRING", (["FOOBARSTRING"], "")),
    ),
)
def test_segment_string(string, expected):
    assert utils.segment_string(string) == expected


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
    assert utils.sanitize_acronyms(acronyms) == expected


@pytest.mark.parametrize(
    "s,i,words,expected",
    (
        # TODO: Add more cases
        (0, 1, ["FOO", "bar"], 0),
        (1, 2, ["foo", "BAR", "baz"], 1),
    ),
)
def test_simple_acronym_detection(s, i, words, expected):
    assert utils.simple_acronym_detection(s, i, words) == expected


@pytest.mark.parametrize(
    "s,i,words,acronyms,expected",
    (
        # TODO: Add more cases
        (0, 1, ["FOO", "bar"], ("FOO",), 0),
        (0, 1, ["FOO", "bar"], ("BAR",), 2),
    ),
)
def test_advanced_acronym_detection(s, i, words, acronyms, expected):
    assert utils.advanced_acronym_detection(s, i, words, acronyms) == expected


@pytest.mark.parametrize("acronyms", ("HT-TP", "NA SA", "SU.GAR"))
def test_sanitize_acronyms_raises_on_invalid_acronyms(acronyms):
    with pytest.raises(InvalidAcronymError):
        utils.sanitize_acronyms(acronyms)


@pytest.mark.parametrize(
    "words,acronyms,expected",
    (
        (["foobar"], (), ["Foobar"]),
        (["fooBar"], (), ["Foobar"]),
        (["FooBar"], (), ["Foobar"]),
        (["Foo", "Bar"], ("BAR"), ["Foo", "BAR"]),
    ),
)
def test_normalize_words(words, acronyms, expected):
    assert utils.normalize_words(words, acronyms) == expected


@pytest.mark.parametrize(
    "words,string,expected",
    (
        ([], "", Case.UNKNOWN),
        (["foobar"], "foobar", Case.LOWER),
        (["foo", "Bar"], "", Case.CAMEL),
        (["Foo", "Bar"], "", Case.PASCAL),
        (["foo", "bar"], "", Case.MIXED),
    ),
)
def test_determine_case(words, string, expected):
    assert utils.determine_case(words=words, string=string) == expected
