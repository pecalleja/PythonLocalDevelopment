import pytest

from src.leetcode.wildcard_matching import Solution


@pytest.mark.parametrize(
    "text, pattern, expected",
    [
        ("aa", "a", False),
        ("aa", "*", True),
        ("cb", "?a", False),
        ("adceb", "*a*b", True),
        ("acdcb", "a*c?b", False),
        ("", "*", True),
        ("", "?", False),
        ("abcdef", "a*f", True),
        ("abcdef", "a*d?f", True),
        ("abcdef", "a*d?g", False),
    ],
)
def test_isMatch(text, pattern, expected):
    solution = Solution()
    assert solution.isMatch(text, pattern) == expected
