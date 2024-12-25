"""
Breadth-First Search for Shortest Path in Binary Matrix

You are provided with a matrix of n×m elements (0s and 1s). You can interpret
1 as a passable cell and 0 as an obstacle. You need to implement a function
bfs_matrix(matrix, start, end), which returns the length of the shortest path
from the start point to the end. The start and end points are tuples (int, int)
indicating the matrix cell (e.g., (0, 0) for the top-left). If the path is
impossible, return 0. It is guaranteed the starting point always contains 1
in the matrix, i.e. there is no obstacle there.

Note: You can only move vertically or horizontally; diagonal movement is
forbidden.

The expected time complexity for the problem is O(n⋅m).
"""

from collections import deque


def solution(matrix, start, end):
    n = len(matrix)  # Number of rows
    if n == 0:
        return 0
    m = len(matrix[0])  # Number of columns

    start_row, start_col = start
    end_row, end_col = end

    # Check if start and end positions are within bounds
    if not (
        0 <= start_row < n
        and 0 <= start_col < m
        and 0 <= end_row < n
        and 0 <= end_col < m
    ):
        return 0

    # Check if end cell is passable
    if matrix[end_row][end_col] == 0:
        return 0

    # Directions: up, down, left, right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # Initialize visited matrix
    visited = [[False for _ in range(m)] for _ in range(n)]
    visited[start_row][start_col] = True

    # Initialize queue with the start cell and distance 0
    queue = deque()
    queue.append((start_row, start_col, 0))

    while queue:
        current_row, current_col, distance = queue.popleft()

        # If we've reached the end cell, return the distance
        if (current_row, current_col) == (end_row, end_col):
            return distance

        # Explore neighbors
        for dr, dc in directions:
            neighbor_row = current_row + dr
            neighbor_col = current_col + dc

            # Check if neighbor is within grid bounds
            if 0 <= neighbor_row < n and 0 <= neighbor_col < m:
                # Check if neighbor is passable and not visited
                if (
                    matrix[neighbor_row][neighbor_col] == 1
                    and not visited[neighbor_row][neighbor_col]
                ):
                    visited[neighbor_row][neighbor_col] = True
                    queue.append((neighbor_row, neighbor_col, distance + 1))

    # If we reach here, no path was found
    return 0
