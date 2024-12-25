"""
Shortest Distance in a City Network Using BFS Algorithm

You are provided with a representation of a network of cities and roads
between them. Each city can be identified by a unique string identifier, and
for each city you are given a set of cities it is connected to by a road.

Your task is to create a function shortest_distance(roads, start, destination)
in Python that extracts the shortest distance from start to destination using
the graph traversal algorithm we discussed in the lesson, the Breadth-First
Search (BFS). If there are no roads leading to the destination, your function
should return None.
"""

from collections import deque


def solution(roads, start, destination):
    if start == destination:
        return 0

    visited = set()  # Track visited cities
    queue = deque([(start, 0)])  # Queue of (city, distance)

    while queue:
        current_city, distance = queue.popleft()
        if current_city in visited:
            continue
        visited.add(current_city)

        for neighbor in roads.get(current_city, []):
            if neighbor == destination:
                return distance + 1
            if neighbor not in visited:
                queue.append((neighbor, distance + 1))

    return None  # No path to the destination
