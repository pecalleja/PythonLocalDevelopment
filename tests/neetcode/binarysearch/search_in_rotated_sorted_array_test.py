import pytest

from src.neetcode.binarysearch.search_in_rotated_sorted_array import Solution


@pytest.mark.parametrize(
    "nums, target, expected",
    [
        ([4, 5, 6, 7, 0, 1, 2], 0, 4),
        ([4, 5, 6, 7, 0, 1, 2], 3, -1),
        ([1], 0, -1),
        ([1, 3], 3, 1),
        ([3, 1], 1, 1),
        ([4, 5, 6, 7, 0, 1, 2], 5, 1),
        ([5, 1, 3], 5, 0),
        ([6, 7, 1, 2, 3, 4, 5], 4, 5),
        ([1, 2, 3, 4, 5, 6, 7], 7, 6),
        ([1, 2, 3, 4, 5, 6, 7], 1, 0),
    ],
)
def test_search(nums, target, expected):
    sol = Solution()
    assert sol.search(nums, target) == expected
