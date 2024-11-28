import pytest

from src.neetcode.binarysearch.median_of_two_sorted_arrays import Solution


@pytest.mark.parametrize(
    "nums1, nums2, expected",
    [
        ([1, 3], [2], 2.0),
        ([1, 2], [3, 4], 2.5),
        ([0, 0], [0, 0], 0.0),
        ([], [1], 1.0),
        ([2], [], 2.0),
        ([1, 3, 8], [7, 9, 10, 11], 8.0),
        ([1, 2, 3, 4], [5, 6, 7, 8, 9], 5.0),
        ([-1, 1], [1, 2, 3], 1.0),
        ([1, 2, 5], [3, 4], 3.0),
    ],
)
def test_findMedianSortedArrays(nums1, nums2, expected):
    solution = Solution()
    assert solution.findMedianSortedArrays(nums1, nums2) == expected
