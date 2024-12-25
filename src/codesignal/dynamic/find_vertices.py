"""
Finding Vertices Within a Given Distance in a Graph

You are given a graph represented as an adjacency list and a starting vertex,
start. The graph is undirected and could be either connected or not connected.
The vertices are labeled with unique positive integers starting from 1. The
task is to implement a function, find_vertices_within_distance
(graph, start, distance), that returns a list of all vertices, sorted in
ascending order by their numbers, whose distance is less than or equal to
distance from the starting vertex. The distance is defined as the minimum
number of edges traversed to get from one vertex to another.

Here is how the graph would be represented in Python:

graph = {
    1: [2, 3],
    2: [1, 4, 5],
    3: [1],
    4: [2],
    5: [2, 6],
    6: [5]
}
Vertices 2 and 3 are adjacent to vertex 1. Vertices 1, 4, and 5 are adjacent
to vertex 2, and so on. For example, if start = 1 and distance = 2, your
function should return [1, 2, 3, 4, 5].

The expected time complexity is O(n), where n is the number of vertices in the
graph.
"""


def solution(graph, start, distance):
    visited = set()
    queue = [(start, 0)]
    result = []
    while queue:
        current_vertex, current_distance = queue.pop(0)
        if current_vertex in visited:
            continue
        visited.add(current_vertex)
        if current_distance <= distance:
            result.append(current_vertex)
            if current_vertex in graph:
                for neighbor in graph[current_vertex]:
                    if neighbor not in visited:
                        queue.append((neighbor, current_distance + 1))
    return sorted(result)
