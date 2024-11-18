import pytest

from src.slidingwindow.permutation_in_string import Solution


@pytest.mark.parametrize(
    "s1, s2, expected",
    [
        ("ab", "eidbaooo", True),
        ("ab", "eidboaoo", False),
        ("abc", "cbaebabacd", True),
        ("a", "a", True),
        ("abc", "def", False),
        ("adc", "dcda", True),
        ("abcd", "abcd", True),
        ("abcd", "dcbae", True),
        ("abcd", "xyz", False),
    ],
)
def test_checkInclusion(s1, s2, expected):
    solution = Solution()
    assert solution.checkInclusion(s1, s2) == expected
