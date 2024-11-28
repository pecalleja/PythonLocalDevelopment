import pytest

from src.neetcode.arrays.group_anagrams import Solution


@pytest.mark.parametrize(
    "strs, expected",
    [
        (
            ["eat", "tea", "tan", "ate", "nat", "bat"],
            [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]],
        ),  # Example 1
        ([""], [[""]]),  # Edge case: empty string
        (["a"], [["a"]]),  # Single character
        (["abc", "bca", "cab"], [["abc", "bca", "cab"]]),  # All are anagrams
        (["abcd", "dcba", "bcda", "dbac"], [["abcd", "dcba", "bcda", "dbac"]]),
        # All are anagrams with 4 chars
        (["abc", "def", "ghi"], [["abc"], ["def"], ["ghi"]]),  # No anagrams
        (["listen", "silent", "enlist"], [["listen", "silent", "enlist"]]),
        # Classic anagram case
        (["bob", "boo", "obb"], [["bob", "obb"], ["boo"]]),
        # One group of anagrams, one non-anagram
        (["abc", "bca", "xyz", "yxz"], [["abc", "bca"], ["xyz", "yxz"]]),
        # Two groups of anagrams
    ],
)
def test_groupAnagrams(strs, expected):
    solution = Solution()
    result = solution.groupAnagrams(strs)

    # Sort the inner lists and outer list for comparison (since order doesn't matter) # noqa
    result_sorted = [sorted(group) for group in sorted(result)]
    expected_sorted = [sorted(group) for group in sorted(expected)]

    assert result_sorted == expected_sorted
