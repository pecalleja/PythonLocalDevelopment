import pytest

from src.leetcode.sorted_rotated import Solution


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([3, 4, 5, 1, 2], True),
        ([2, 1, 3, 4], False),
        ([1, 2, 3, 4, 5], True),
        ([1, 1, 1, 1, 1], True),
        ([2, 3, 4, 5, 1], True),
        ([3, 2, 1], False),
        ([1], True),
        ([1, 2], True),
        ([2, 1], True),
        ([1, 3, 2], False),
        ([5, 6, 7, 1, 2, 3, 4], True),
        ([7, 9, 1, 2, 3, 4, 5], True),
        ([4, 5, 6, 7, 8, 9, 10, 1, 2, 3], True),
    ],
)
def test_check(nums, expected):
    assert Solution().check(nums) == expected
