import pytest

from src.slidingwindow.longest_substring_without_repeating_characters import (
    Solution,
)


@pytest.mark.parametrize(
    "s, expected",
    [
        ("abcabcbb", 3),  # "abc"
        ("bbbbb", 1),  # "b"
        ("pwwkew", 3),  # "wke"
        ("", 0),  # Empty string
        (" ", 1),  # Single space
        ("dvdf", 3),  # "vdf"
        ("anviaj", 5),  # "nviaj"
        ("aab", 2),  # "ab"
        ("tmmzuxt", 5),  # "mzuxt"
    ],
)
def test_lengthOfLongestSubstring(s, expected):
    solution = Solution()
    assert solution.lengthOfLongestSubstring(s) == expected
