import pytest

from src.codesignal.graphs.shortest_path import solution


@pytest.mark.parametrize(
    "grid, source, destination, expected",
    [
        (
            [
                [True, True, False, True],
                [False, True, True, False],
                [True, True, False, True],
                [True, False, True, True],
            ],
            (0, 0),
            (3, 3),
            (-1, []),
        ),
        (
            [
                [True, False, False, False],
                [True, True, True, True],
                [False, False, False, True],
                [False, False, False, True],
            ],
            (0, 0),
            (3, 3),
            (6, [(0, 0), (1, 0), (1, 1), (1, 2), (1, 3), (2, 3), (3, 3)]),
        ),
        ([[True]], (0, 0), (0, 0), (0, [(0, 0)])),
        (
            [[True, True], [False, True]],
            (0, 0),
            (1, 1),
            (2, [(0, 0), (0, 1), (1, 1)]),
        ),
        (
            [
                [True, True, False, True],
                [False, True, False, True],
                [False, False, False, True],
                [True, True, True, True],
            ],
            (0, 0),
            (3, 3),
            (-1, []),
        ),
    ],
)
def test_shortest_path(grid, source, destination, expected):
    assert solution(grid, source, destination) == expected
