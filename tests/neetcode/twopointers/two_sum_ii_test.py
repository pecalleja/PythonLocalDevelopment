import pytest

from src.neetcode.twopointers.two_sum_ii import Solution


@pytest.mark.parametrize(
    "numbers, target, expected",
    [
        ([2, 7, 11, 15], 9, [1, 2]),
        ([2, 3, 4], 6, [1, 3]),
        ([-1, 0], -1, [1, 2]),
        ([1, 2, 3, 4, 4], 8, [4, 5]),
        ([1, 3, 4, 5, 7, 10, 11], 9, [3, 4]),
        ([1, 2, 3, 4, 5], 10, []),
        ([1, 5, 6, 8, 11], 12, [1, 5]),
    ],
)
def test_twoSum(numbers, target, expected):
    sol = Solution()
    assert sol.twoSum(numbers, target) == expected
