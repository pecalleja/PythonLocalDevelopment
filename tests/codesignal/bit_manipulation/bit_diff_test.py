import pytest

from src.codesignal.bit_manipulation.bit_diff import solution


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (14, 15, 1),
        (10, 10, 0),
        (0, 0, 0),
        (1, 0, 1),
        (0, 1, 1),
        (1234, 5678, 8),
        (7, 11, 2),
        (2**30, 2**30 - 1, 31),
        (2**30 - 1, 2**30, 31),
        (1, 2**30, 2),
        (2**30, 1, 2),
    ],
)
def test_solution(a, b, expected):
    assert solution(a, b) == expected
