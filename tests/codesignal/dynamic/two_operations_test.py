import pytest

from src.codesignal.dynamic.two_operations import min_steps


@pytest.mark.parametrize(
    "n, expected",
    [
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 3),
        (5, 4),
        (10, 5),
        (15, 7),
        (20, 6),
        (50, 8),
        (100, 9),
        (200, 10),
        (500, 14),
        (1000, 15),
        (17, 6),
        (321, 11),
        (888, 15),
    ],
)
def test_min_steps(n, expected):
    assert min_steps(n) == expected
