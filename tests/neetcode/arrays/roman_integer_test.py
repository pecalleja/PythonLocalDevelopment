import pytest

from src.neetcode.arrays.roman_integer import Solution


@pytest.mark.parametrize(
    "s, expected",
    [
        ("III", 3),
        ("IV", 4),
        ("IX", 9),
        ("LVIII", 58),
        ("MCMXCIV", 1994),
        ("XLII", 42),
        ("LXXVII", 77),
        ("DCCCXLV", 845),
        ("MMMCMXCIX", 3999),
        ("I", 1),
        ("", 0),
        ("MDCLXVI", 1666),
    ],
)
def test_romanToInt(s, expected):
    solution = Solution()
    assert solution.romanToInt(s) == expected


@pytest.mark.parametrize(
    "num, expected",
    [
        (3, "III"),
        (4, "IV"),
        (9, "IX"),
        (58, "LVIII"),
        (1994, "MCMXCIV"),
        (3999, "MMMCMXCIX"),
    ],
)
def test_int_to_roman(num, expected):
    solution = Solution()
    assert solution.intToRoman(num) == expected
