import pytest

from src.neetcode.binarysearch.binary_search import Solution


@pytest.mark.parametrize(
    "nums, target, expected",
    [
        ([1, 2, 3, 4, 5, 6], 4, 3),  # Target in the middle of the list
        ([1, 2, 3, 4, 5, 6], 1, 0),  # Target at the start
        ([1, 2, 3, 4, 5, 6], 6, 5),  # Target at the end
        ([1, 3, 5, 7, 9, 11], 2, -1),  # Target not in the list
        ([], 5, -1),  # Empty list
        ([5], 5, 0),  # Single element list, target found
        ([5], 4, -1),  # Single element list, target not found
        ([1, 3, 5, 7, 9], 7, 3),  # Odd length list
        ([-10, -3, 0, 5, 9], 0, 2),  # List with negative and positive numbers
        ([-10, -3, 0, 5, 9], -3, 1),  # Target is a negative number
    ],
)
def test_search(nums, target, expected):
    sol = Solution()
    assert sol.search(nums, target) == expected
