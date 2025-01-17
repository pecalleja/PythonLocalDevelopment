import heapq


def solution(grid, source, destination):
    n = len(grid)  # Assuming the grid is n x n

    if (
        not grid[source[0]][source[1]]
        or not grid[destination[0]][destination[1]]
    ):
        return -1, []  # If source or destination is blocked

    # Directions for movement: up, down, left, right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # Priority queue for Dijkstra's algorithm
    pq = [(0, source, [source])]  # (distance, current_node, path)
    visited = set()

    while pq:
        dist, current, path = heapq.heappop(pq)

        if current in visited:
            continue
        visited.add(current)

        if current == destination:
            return dist, path  # Return distance and path

        for direction in directions:
            new_x = current[0] + direction[0]
            new_y = current[1] + direction[1]

            if (
                0 <= new_x < n
                and 0 <= new_y < n
                and grid[new_x][new_y]
                and (new_x, new_y) not in visited
            ):
                new_path = path + [(new_x, new_y)]
                heapq.heappush(pq, (dist + 1, (new_x, new_y), new_path))

    return -1, []  # If no path exists
