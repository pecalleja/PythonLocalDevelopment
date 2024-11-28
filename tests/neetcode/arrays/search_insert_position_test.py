import pytest

from src.neetcode.arrays.search_insert_position import Solution


@pytest.mark.parametrize(
    "nums, target, expected",
    [
        ([1, 3, 5, 6], 5, 2),
        ([1, 3, 5, 6], 2, 1),
        ([1, 3, 5, 6], 7, 4),
        ([1, 3, 5, 6], 0, 0),
        ([1], 0, 0),
        ([1], 2, 1),
        ([], 1, 0),
        ([1, 3, 5, 6, 8, 9], 4, 2),
        ([1, 2, 3, 4, 5, 6], 4, 3),
    ],
)
def test_searchInsert(nums, target, expected):
    solution = Solution()
    result = solution.searchInsert(nums, target)

    # Assert the result is as expected
    assert result == expected
