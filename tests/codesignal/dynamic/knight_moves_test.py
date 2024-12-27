import pytest

from src.codesignal.dynamic.knight_moves import solution


@pytest.mark.parametrize(
    "board, start, end, expected",
    [
        ([[0] * 8 for _ in range(8)], (0, 0), (7, 7), 6),
        ([[0] * 8 for _ in range(8)], (0, 0), (0, 0), 0),
        ([[0] * 8 for _ in range(8)], (7, 7), (7, 7), 0),
        ([[0] * 8 for _ in range(8)], (4, 4), (6, 6), 4),
        ([[0] * 8 for _ in range(8)], (4, 4), (2, 2), 4),
        ([[0] * 8 for _ in range(8)], (7, 0), (0, 7), 6),
        ([[0] * 8 for _ in range(8)], (3, 3), (3, 6), 3),
        ([[0] * 8 for _ in range(8)], (2, 2), (5, 2), 3),
        ([[0] * 8 for _ in range(8)], (4, 5), (2, 1), 2),
        ([[0] * 8 for _ in range(8)], (7, 0), (0, 0), 5),
        ([[0] * 8 for _ in range(8)], (7, 7), (0, 0), 6),
    ],
)
def test_knight_moves(board, start, end, expected):
    assert solution(board, start, end) == expected
