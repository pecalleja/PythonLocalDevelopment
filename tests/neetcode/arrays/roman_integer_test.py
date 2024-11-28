import pytest

from src.neetcode.arrays.roman_integer import Solution


# fmt: off
@pytest.mark.parametrize("s, expected", [
    ("III", 3),           # Simple case: III = 3
    ("IV", 4),            # Subtractive notation: IV = 4
    ("IX", 9),            # Subtractive notation: IX = 9
    ("LVIII", 58),        # L = 50, V = 5, III = 3 -> 50 + 5 + 3 = 58
    ("MCMXCIV", 1994),    # M = 1000, CM = 900, XC = 90, IV = 4 -> 1000 + 900 + 90 + 4 = 1994  # noqa
    ("XLII", 42),         # XL = 40, II = 2 -> 40 + 2 = 42
    ("LXXVII", 77),       # L = 50, XX = 20, VII = 7 -> 50 + 20 + 7 = 77
    ("DCCCXLV", 845),     # D = 500, CCC = 300, XL = 40, V = 5 -> 500 + 300 + 40 + 5 = 845  # noqa
    ("MMMCMXCIX", 3999),  # Largest Roman numeral: 3999
    ("I", 1),             # Smallest Roman numeral: 1
    ("", 0),              # Empty string should return 0
    ("MDCLXVI", 1666),    # M = 1000, D = 500, C = 100, L = 50, X = 10, V = 5, I = 1 -> 1666  # noqa
])
# fmt: on
def test_romanToInt(s, expected):
    solution = Solution()
    assert solution.romanToInt(s) == expected
