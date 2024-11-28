import pytest

from src.neetcode.slidingwindow.minimum_window_substring import Solution


@pytest.mark.parametrize(
    "s, t, expected",
    [
        ("ADOBECODEBANC", "ABC", "BANC"),
        ("a", "a", "a"),
        ("a", "aa", ""),
        ("AA", "AA", "AA"),
        ("aaflslflsldkabc", "abc", "abc"),
        ("", "A", ""),
        ("A", "", ""),
        ("ab", "A", ""),
        ("ADOBECODEBANC", "AABC", "ADOBECODEBA"),
    ],
)
def test_minWindow(s, t, expected):
    solution = Solution()
    assert solution.minWindow(s, t) == expected
