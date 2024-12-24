import pytest

from src.codesignal.trees.shortest_route import solution


@pytest.mark.parametrize(
    "distance, stride_length, obstacles, expected",
    [
        (10, 3, [3, 6, 8], 4),
        (20, 2, [1, 3, 5, 7, 9, 11, 13, 15, 17], 10),
        (20, 2, [2, 4, 6, 8, 10, 12, 14, 16, 18], 10),
        (20, 5, [2, 7, 9, 12, 17], 4),
        (20, 5, [4, 9, 14, 19], -1),
        (20, 3, [], 7),
        (100, 3, [i for i in range(1, 100, 2)], -1),
        (100, 10, [10, 20, 30, 40, 50, 60, 70, 80, 90], 10),
        (100, 2, [i for i in range(0, 100, 2)], 50),
        (4, 3, [2], 1),
        (4, 3, [], 1),
        (2, 1, [], 1),
        (2, 1, [1], -1),
    ],
)
def test_shortest_route(distance, stride_length, obstacles, expected):
    assert solution(distance, stride_length, obstacles) == expected
