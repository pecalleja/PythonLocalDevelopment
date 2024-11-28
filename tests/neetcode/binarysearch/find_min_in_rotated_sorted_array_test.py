import pytest

from src.neetcode.binarysearch.find_min_in_rotated_sorted_array import Solution


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([3, 4, 5, 1, 2], 1),  # Rotated array with minimum at the end
        ([4, 5, 6, 7, 0, 1, 2], 0),  # Rotated array with minimum in the middle
        ([11, 13, 15, 17], 11),  # Non-rotated array
        ([2, 1], 1),  # Small rotated array
        ([1, 2, 3, 4, 5], 1),  # Already sorted array
        ([5, 6, 7, 1, 2, 3, 4], 1),  # Rotated array with multiple elements
        ([10], 10),  # Single element array
        ([3, 1, 2], 1),  # Small rotated array
        ([2, 3, 4, 5, 1], 1),  # Minimum at the end
    ],
)
def test_find_min(nums, expected):
    sol = Solution()
    assert sol.findMin(nums) == expected
