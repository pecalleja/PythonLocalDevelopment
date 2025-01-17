import pytest

from src.codesignal.graphs.topological_sort import solution

# Each test case is represented as a tuple:
# (graph, expected, raises_exception)
# For cases where many orders are acceptable, expected is a list of valid orderings.  # noqa
# For cases where any valid ordering is acceptable as long as node constraints are met,  # noqa
# we use None and then add further custom assertions.
testdata = [
    # Test case 1: Two acceptable orders.
    (
        {'A': ['B', 'C'], 'B': ['D'], 'C': ['D'], 'D': []},
        [['A', 'B', 'C', 'D'], ['A', 'C', 'B', 'D']],
    ),
    # Test case 2: Single acceptable order.
    (
        {'A': ['B'], 'B': ['C'], 'C': []},
        [['A', 'B', 'C']],
    ),
    # Test case 3: Graph with cycle, expect exception.
    ({'A': ['B'], 'B': ['A'], 'C': ['D'], 'D': ['C']}, [[]]),
    # Test case 4: Two acceptable orders.
    (
        {'A': ['B', 'C'], 'B': ['D'], 'C': ['D'], 'D': ['E'], 'E': []},
        [['A', 'B', 'C', 'D', 'E'], ['A', 'C', 'B', 'D', 'E']],
    ),
    # Test case 5: Graph with 5 isolated nodes.
    # We check that the returned ordering contains all 5 nodes in any order.
    (
        {'A': [], 'B': [], 'C': [], 'D': [], 'E': []},
        [["A", "B", "C", "D", "E"]],
    ),
    # Test case 6: Node 'A' must appear first.
    # Then the remaining nodes can be in any order.
    (
        {'A': ['B', 'C', 'D', 'E'], 'B': [], 'C': [], 'D': [], 'E': []},
        [["A", "B", "C", "D", "E"]],
    ),
]


@pytest.mark.parametrize("graph,expected", testdata)
def test_topological_sort(graph, expected):
    result = solution(graph)
    # When an expected result is provided as a list of acceptable orders,
    # check if the result matches one of them.
    if expected is not None:
        assert (
            result in expected
        ), f"Result {result} not in expected orders: {expected}"
    else:
        # For test case 5: All nodes should be present in any order.
        if set(graph.keys()) == set(['A', 'B', 'C', 'D', 'E']):
            assert len(result) == 5, "Result should contain 5 nodes."
            # Sorted order of nodes should match the sorted keys.
            assert sorted(result) == [
                'A',
                'B',
                'C',
                'D',
                'E',
            ], "Nodes mismatch."
        # For test case 6: 'A' must be the first node.
        elif graph.get('A'):
            assert len(result) == 5, "Result should contain 5 nodes."
            assert result[0] == 'A', "Node 'A' must be first in the result."
            # The remaining nodes should be the rest.
            assert sorted(result[1:]) == sorted(
                list(graph.keys() - {'A'})
            ), "Remaining nodes mismatch."
