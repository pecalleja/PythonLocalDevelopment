import pytest

from src.codesignal.graphs.shortest_path_distance import solution


@pytest.mark.parametrize(
    "graph, start, end, expected",
    [
        (
            {
                'JFK': {'LAX': 2500, 'MIA': 2000, 'ORD': 1200},
                'LAX': {'SEA': 2000, 'ORD': 3000},
                'MIA': {'ORD': 1500, 'ATL': 2000, 'DFW': 1800},
                'ORD': {'SEA': 2800},
                'SEA': {},
                'ATL': {'DFW': 1500},
                'DFW': {},
            },
            'JFK',
            'SEA',
            4000,
        ),
        (
            {
                'JFK': {'LAX': 2500, 'MIA': 2000, 'ORD': 1200},
                'LAX': {'SEA': 2000, 'ORD': 3000},
                'MIA': {'ORD': 1500, 'ATL': 2000, 'DFW': 1800},
                'ORD': {'SEA': 2800},
                'SEA': {},
                'ATL': {'DFW': 1500},
                'DFW': {},
            },
            'ORD',
            'ORD',
            0,
        ),
        (
            {
                'A': {'B': 10},
                'B': {'A': 10},
            },
            'A',
            'B',
            10,
        ),
        ({'A': {'B': 1, 'C': 10}, 'B': {'C': 1}, 'C': {}}, 'A', 'C', 2),
        (
            {
                'A': {'B': 3, 'C': 2},
                'B': {'D': 2},
                'C': {'B': 1, 'D': 1},
                'D': {},
            },
            'A',
            'D',
            3,
        ),
        (
            {
                'A': {'B': 30, 'C': 20, 'D': 10},
                'B': {'E': 60},
                'C': {'E': 50},
                'D': {'E': 40},
                'E': {},
            },
            'A',
            'E',
            50,
        ),
        (
            {
                'A': {'B': 5, 'C': 10},
                'B': {'C': 2, 'D': 20},
                'C': {'D': 10},
                'D': {},
            },
            'A',
            'D',
            17,
        ),
    ],
)
def test_shortest_path(graph, start, end, expected):
    assert solution(graph, start, end) == expected
