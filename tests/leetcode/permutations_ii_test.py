import pytest

from src.leetcode.permutations_ii import Solution


# fmt: off
@pytest.mark.parametrize("nums, expected", [
    (
        [1, 1, 2], [[1, 1, 2], [1, 2, 1], [2, 1, 1]]
    ), (
        [1, 2, 3], [
            [1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]
        ]
    ), (
        [1, 1, 1], [[1, 1, 1]]
    ), (
        [], [[]]
    ), (
        [0], [[0]]
    )
])
# fmt: on
def test_permuteUnique(nums, expected):
    result = Solution().permuteUnique(nums)
    assert sorted(result) == sorted(expected)
