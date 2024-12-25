import pytest

from src.neetcode.backtracking.combination_sum_ii import Solution


@pytest.mark.parametrize(
    "candidates, target, expected",
    [
        ([10, 1, 2, 7, 6, 1, 5], 8, [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]),
        ([2, 5, 2, 1, 2], 5, [[1, 2, 2], [5]]),
        ([2], 1, []),
        ([], 3, []),
        ([1, 1, 1, 1, 1], 2, [[1, 1]]),
        ([3], 3, [[3]]),
    ],
)
def test_combinationSum2(candidates, target, expected):
    solution = Solution()
    result = solution.combinationSum2(candidates, target)
    result_sorted = sorted([sorted(comb) for comb in result])
    expected_sorted = sorted([sorted(comb) for comb in expected])

    assert result_sorted == expected_sorted
