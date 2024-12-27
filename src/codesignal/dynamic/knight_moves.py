"""
Minimum Knight Moves on a Chessboard

In this problem, you are given a standard 8×8 chessboard and two cells on the
board — the start and the end cells. The aim is to calculate the minimum
number of moves it would take for a chess knight to get from the given start
cell to the end cell.
Your function should return the minimum number of moves the knight needs to
get from the start cell to the end cell. Both start and end points are given
0-based (all coordinates are from 0 to 7).
"""

from collections import deque


def solution(board, start, end):
    n = len(board)
    m = len(board[0])

    start_row, start_col = start
    end_row, end_col = end

    directions = [
        (-2, -1),
        (-2, 1),
        (-1, -2),
        (-1, 2),
        (1, -2),
        (1, 2),
        (2, -1),
        (2, 1),
    ]

    visited = [[False for _ in range(m)] for _ in range(n)]
    visited[start_row][start_col] = True

    queue = deque()
    queue.append((start_row, start_col, 0))

    while queue:
        current_row, current_col, distance = queue.popleft()

        if (current_row, current_col) == (end_row, end_col):
            return distance

        for dr, dc in directions:
            neighbor_row = current_row + dr
            neighbor_col = current_col + dc

            if 0 <= neighbor_row < n and 0 <= neighbor_col < m:
                if not visited[neighbor_row][neighbor_col]:
                    visited[neighbor_row][neighbor_col] = True
                    queue.append((neighbor_row, neighbor_col, distance + 1))

    return -1
