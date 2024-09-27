import pytest

from src.arrays.contains_duplicate import Solution


# fmt: off
@pytest.mark.parametrize(
    "nums, expected",
    [
        ([1, 2, 3, 4], False),  # All elements are unique
        ([1, 2, 3, 1], True),  # Duplicate element 1
        ([1, 1, 1, 1], True),  # All elements are the same
        ([], False),  # Empty array, no duplicates
        ([1], False),  # Single element, no duplicates
        ([1, 2, 3, 4, 5, 6, 7, 8, 9], False),  # No duplicates in a long list
        ([1000000, 2000000, 3000000, 1000000], True),  # Duplicates in large numbers # noqa
        ([-1, -2, -3, -1], True),  # Negative number duplicates
        ([-1, -2, -3, -4], False),  # Negative numbers, no duplicates
        ([0, 0, 1], True),  # Duplicates with zero
        ([0, 1, 2, 3, 4], False),  # Includes zero but no duplicates
        ([2**31 - 1, 2**31 - 1], True),  # Maximum int value, duplicate
        ([-(2**31), -(2**31)], True),  # Minimum int value, duplicate
    ],
)
# fmt: on
def test_contains_duplicate(nums, expected):
    assert Solution().containsDuplicate(nums) == expected
