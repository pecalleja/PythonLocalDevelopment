import pytest

from src.codesignal.dynamic.min_sum_perfect_square import solution


@pytest.mark.parametrize(
    "n, expected",
    [
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 1),
        (12, 3),
        (13, 2),
        (100, 1),
        (999, 4),
        (1000, 2),
        (9999, 4),
        (10000, 1),
    ],
)
def test_solution(n, expected):
    assert solution(n) == expected
