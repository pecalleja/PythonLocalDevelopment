import pytest

from src.neetcode.backtracking.combination_sum import Solution


@pytest.mark.parametrize(
    "candidates, target, expected",
    [
        ([2, 3, 6, 7], 7, [[2, 2, 3], [7]]),
        ([2, 3, 5], 8, [[2, 2, 2, 2], [2, 3, 3], [3, 5]]),
        ([2], 1, []),
        ([], 7, []),
        ([2, 3, 6, 7], 0, [[]]),
    ],
)
def test_combination_sum(candidates, target, expected):
    solution = Solution()
    result = solution.combinationSum(candidates, target)
    assert sorted(result) == sorted(expected)
