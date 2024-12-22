import pytest

from src.codesignal.trees.shortest_distance import solution


@pytest.mark.parametrize(
    "roads, start, destination, expected",
    [
        (
            {'A': {'B'}, 'B': {'C', 'A'}, 'C': {'B'}, 'D': {'E'}, 'E': {'D'}},
            'A',
            'D',
            None,
        ),
        ({'A': {'B'}, 'B': {'C', 'A'}, 'C': {'B'}}, 'A', 'C', 2),
        ({'A': {'B'}, 'B': {'A'}}, 'A', 'B', 1),
        (
            {
                'A': {'B'},
                'B': {'D', 'C', 'A'},
                'C': {'B'},
                'D': {'E', 'B'},
                'E': {'D'},
            },
            'A',
            'E',
            3,
        ),
        ({'A': {'C', 'B'}, 'B': {'A'}, 'C': {'A'}}, 'B', 'C', 2),
        (
            {
                'A': {'C', 'B'},
                'B': {'D', 'A'},
                'C': {'E', 'A'},
                'D': {'F', 'B'},
                'E': {'C'},
                'F': {'D'},
            },
            'A',
            'F',
            3,
        ),
        ({'A': {'B'}, 'B': {'C', 'A'}, 'C': {'B'}}, 'A', 'A', 0),
        (
            {'A': {'D', 'C', 'B'}, 'B': {'A'}, 'C': {'A'}, 'D': {'A'}},
            'A',
            'D',
            1,
        ),
        (
            {
                'A': {'B'},
                'B': {'D', 'C', 'E', 'A'},
                'C': {'B'},
                'D': {'B'},
                'E': {'B'},
            },
            'A',
            'E',
            2,
        ),
        ({'A': {}, 'B': {}, 'C': {}, 'D': {}, 'E': {}}, 'A', 'E', None),
    ],
)
def test_shortest_distance(roads, start, destination, expected):
    assert solution(roads, start, destination) == expected
