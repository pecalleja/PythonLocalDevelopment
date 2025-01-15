from typing import List

import pytest

from src.leetcode.n_queens import Solution


@pytest.mark.parametrize(
    "n, expected_count, expected_boards",
    [
        (1, 1, [["Q"]]),
        (
            4,
            2,
            [
                [".Q..", "...Q", "Q...", "..Q."],
                ["..Q.", "Q...", "...Q", ".Q.."],
            ],
        ),
    ],
)
def test_solve_nqueens(
    n: int, expected_count: int, expected_boards: List[List[str]]
):
    solutions = Solution().solveNQueens(n)

    # Check that the number of solutions matches the expected count.
    assert (
        len(solutions) == expected_count
    ), f"For n = {n}, expected {expected_count} solutions but got {len(solutions)}."  # noqa

    # Because the order in which the solutions are returned does not matter,
    # we check that every expected board is found in the returned solutions.
    for expected_board in expected_boards:
        assert (
            expected_board in solutions
        ), f"Expected board configuration:\n{expected_board}\nnot found in the solutions."  # noqa
