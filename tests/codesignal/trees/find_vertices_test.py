import pytest

from src.codesignal.trees.find_vertices import solution


@pytest.mark.parametrize(
    "graph, start, distance, expected",
    [
        (
            {1: [2, 3], 2: [1, 4, 5], 3: [1], 4: [2], 5: [2, 6], 6: [5]},
            1,
            2,
            [1, 2, 3, 4, 5],
        ),
        ({1: [2], 2: [1, 3], 3: [2]}, 1, 2, [1, 2, 3]),
        ({1: [2], 2: [1, 3], 3: [2]}, 1, 1, [1, 2]),
        ({1: [2], 2: [1, 3, 4], 3: [2], 4: [2]}, 1, 2, [1, 2, 3, 4]),
        ({1: []}, 1, 0, [1]),
        ({1: [2, 3, 4, 5]}, 1, 1, [1, 2, 3, 4, 5]),
        ({1: [2], 2: [1]}, 1, 0, [1]),
        ({1: [2], 2: [1]}, 1, 1000, [1, 2]),
        ({n: [n + 1] for n in range(1, 1000)}, 1, 1, [1, 2]),
        (
            {**{n: [n + 1] for n in range(1, 1000)}, 1000: []},
            1,
            1000,
            list(range(1, 1001)),
        ),
    ],
)
def test_find_vertices_within_distance(graph, start, distance, expected):
    assert solution(graph, start, distance) == expected
