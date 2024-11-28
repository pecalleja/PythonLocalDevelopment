import pytest

from src.neetcode.linkedlists.linked_list_cycle import Solution


@pytest.mark.parametrize(
    "values, pos, expected",
    [
        (
            [3, 2, 0, -4],
            1,
            True,
        ),  # Cycle exists (last node connects to second node)
        (
            [1, 2],
            0,
            True,
        ),  # Cycle exists (last node connects to the first node)
        ([1], None, False),  # Single node, no cycle
        ([], None, False),  # Empty list, no cycle
        ([1, 2, 3, 4], None, False),  # Multiple nodes, no cycle
    ],
)
def test_hasCycle(build_linked_list, values, pos, expected):
    sol = Solution()
    head = build_linked_list(values, pos)
    assert sol.hasCycle(head) == expected
