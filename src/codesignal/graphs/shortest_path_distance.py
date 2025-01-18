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
