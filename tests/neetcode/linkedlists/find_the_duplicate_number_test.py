import pytest

from src.neetcode.linkedlists.find_the_duplicate_number import Solution


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([1, 3, 4, 2, 2], 2),
        ([3, 1, 3, 4, 2], 3),
        ([1, 1], 1),
        ([1, 1, 2], 1),
        ([2, 2, 2, 2, 2], 2),
    ],
)
def test_findDuplicate(nums, expected):
    solution = Solution()
    assert solution.findDuplicate(nums) == expected
