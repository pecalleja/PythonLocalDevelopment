from collections import deque


def solution(graph):
    # Initialize in-degree of each node to 0.
    in_degree = {node: 0 for node in graph}

    # Compute in-degrees.
    # This loop also accounts for nodes that might appear only as neighbors.
    for node in graph:
        for neighbor in graph[node]:
            if neighbor not in in_degree:
                in_degree[neighbor] = 0
            in_degree[neighbor] += 1

    # Collect nodes with in-degree 0.
    queue = deque([node for node, degree in in_degree.items() if degree == 0])

    # List to store the topological order.
    topo_order = []

    while queue:
        current = queue.popleft()
        topo_order.append(current)

        # Decrease the in-degree for all neighbors.
        for neighbor in graph.get(current, []):
            in_degree[neighbor] -= 1
            # If in-degree becomes 0, add it to the queue.
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # Check if topological order includes all nodes.
    if len(topo_order) != len(in_degree):
        return []

    return topo_order
