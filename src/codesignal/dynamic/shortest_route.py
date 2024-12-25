"""
Find the Shortest Route in a Game Using BFS Algorithm


Imagine you are an adventurous character in a video game who needs to travel
from the start point to the end point in a straight line while avoiding
various obstacles. The distance between the two points is given in terms of
the number of steps. You can cover 1 to stride_length steps in a single stride.
However, some points have obstacles, and you cannot step on them. If you
reach an obstacle, you have to decide whether to make a shorter stride or go
past it if possible. Your aim is to minimize the number of strides you take,
and you are asked to find the shortest route. You need to implement this
solution using the Breadth-First Search (BFS) algorithm.

Your task is to calculate the minimal number of steps you need to take to get
from starting point 0 to the end point distance - 1. If there is no such path
from the start to the end, return -1.

For example, given the distance = 11, and you can stride 1 to 3 steps at a
time, the obstacles are on the 4th, 7th, and 9th steps. As you cannot step on
them, you need to calculate the minimum strides to get from 0 to distance
- 1 = 10, ensuring you do not step on the 4th, 7th, and 9th steps - in this
case, it'd be 0 -> 3 -> 6 -> 8 -> 10, which is 4 steps in total.

The expected time complexity is O(distance⋅stride_length).
"""

from collections import deque


def solution(distance, stride_length, obstacles):
    # Convert obstacles to a set for quick lookups
    obstacle_set = set(obstacles)

    # BFS queue stores tuples: (current_position, stride_count)
    queue = deque([(0, 0)])  # Start at position 0 with 0 strides

    # Visited set to avoid reprocessing the same position
    visited = {0}

    while queue:
        current_position, strides = queue.popleft()

        # Check if we've reached the end point
        if current_position == distance - 1:
            return strides

        # Try all possible strides from 1 to stride_length
        for step in range(1, stride_length + 1):
            next_position = current_position + step

            # Check if the next position is valid
            if (
                next_position < distance
                and next_position not in obstacle_set
                and next_position not in visited
            ):
                visited.add(next_position)
                queue.append((next_position, strides + 1))

    # If we exhaust the queue without reaching the end point, return -1
    return -1
