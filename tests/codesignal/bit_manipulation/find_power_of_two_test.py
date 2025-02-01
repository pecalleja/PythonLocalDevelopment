import pytest

from src.codesignal.bit_manipulation.find_power_of_two import solution


@pytest.mark.parametrize(
    "n, expected",
    [
        (1, True),
        (2, True),
        (3, False),
        (4, True),
        (5, False),
        (6, False),
        (7, False),
        (8, True),
        (9, False),
        (10, False),
        (16, True),
        (32, True),
        (64, True),
        (128, True),
        (256, True),
        (512, True),
        (1024, True),
        (2048, True),
        (4096, True),
        (8192, True),
    ],
)
def test_solution(n, expected):
    assert solution(n) == expected
