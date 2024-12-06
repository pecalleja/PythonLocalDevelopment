import pytest

from src.codesignal.string_manipulation.swapping_character import solution


@pytest.mark.parametrize(
    "input_string, expected_output",
    [
        ("abcdef", "badcfe"),
        ("hello", "ehllo"),
        ("H", "H"),
        ("", ""),
        ("123456", "214365"),
        ("!@#$%^&", "@!$#^%&"),
        ("abcde" * 20, "badcaecbed" * 10),
        ("!!!!!", "!!!!!"),
        ("a" * 99 + "b", ("a" * 98) + "ba"),
    ],
)
def test_solution(input_string, expected_output):
    assert solution(input_string) == expected_output
