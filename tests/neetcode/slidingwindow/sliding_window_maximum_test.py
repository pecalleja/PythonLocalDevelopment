import pytest

from src.neetcode.slidingwindow.sliding_window_maximum import Solution


@pytest.mark.parametrize(
    "nums, k, expected",
    [
        ([1, 3, -1, -3, 5, 3, 6, 7], 3, [3, 3, 5, 5, 6, 7]),
        ([1], 1, [1]),
        ([1, -1], 1, [1, -1]),
        ([9, 11], 2, [11]),
        ([4, -2], 2, [4]),
        ([1, 3, 1, 2, 0, 5], 3, [3, 3, 2, 5]),
        ([1, 3, 1, 2, 0, 5], 1, [1, 3, 1, 2, 0, 5]),
        ([10, 9, 8, 7, 6], 2, [10, 9, 8, 7]),
        ([1, 2, 3, 4, 5], 2, [2, 3, 4, 5]),
        ([], 3, []),
        ([1, 3, -1, -3, 5, 3, 6, 7], 8, [7]),
    ],
)
def test_maxSlidingWindow(nums, k, expected):
    solution = Solution()
    assert solution.maxSlidingWindow(nums, k) == expected
