"""
Finding the Shortest Flight Path Using Dijkstra's Algorithm
Given the flight map of a city, represented as a dictionary, where the key
represents the name of the airport (as a string) and the corresponding value
is another dictionary. In the second dictionary, the key represents the name
of an airport directly reachable from the first airport, and the corresponding
value represents the air distance (in km) between these two airports.
Implement Dijkstra’s Algorithm to find the air distance of the shortest path
between any two given airports. The function should return the corresponding
distance. It is guaranteed the path from start to end always exists.

For instance:

```python
graph = {
    'JFK': {'LAX': 2500, 'MIA': 2000, 'ORD': 1200},
    'LAX': {'SEA': 2000, 'ORD': 3000},
    'MIA': {'ORD': 1500, 'ATL': 2000, 'DFW': 1800},
    'ORD': {'SEA': 2800},
    'SEA': {},
    'ATL': {'DFW': 1500},
    'DFW': {}
}
```
Here, JFK, LAX, MIA, and others are names of airports, and distances are in
kilometers (km).

"""

import heapq


def solution(graph, start, end):
    distances = {airport: float('inf') for airport in graph}
    distances[start] = 0

    # Priority queue to explore the graph.
    # Each item is a tuple (current_distance, airport)
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_airport = heapq.heappop(priority_queue)

        # If we reached the destination, we can return the distance.
        if current_airport == end:
            return current_distance

        # If we found a better path before, skip processing this one.
        if current_distance > distances[current_airport]:
            continue

        # Explore neighbors of the current airport.
        for neighbor, weight in graph[current_airport].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances[end]
