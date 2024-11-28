import pytest

from src.neetcode.linkedlists.copy_list_with_random_pointer import Node
from src.neetcode.linkedlists.copy_list_with_random_pointer import Solution


def list_to_linked_list_with_random(nodes):
    if not nodes:
        return None

    node_map = {}
    head = Node(nodes[0][0])
    node_map[0] = head
    current = head

    for i in range(1, len(nodes)):
        new_node = Node(nodes[i][0])
        node_map[i] = new_node
        current.next = new_node
        current = new_node

    current = head
    for i, (_, random_idx) in enumerate(nodes):
        if random_idx is not None:
            current.random = node_map[random_idx]
        current = current.next

    return head


def linked_list_with_random_to_list(head):
    if not head:
        return []

    index_map = {}
    current = head
    idx = 0
    while current:
        index_map[current] = idx
        current = current.next
        idx += 1

    current = head
    result = []
    while current:
        random_idx = index_map[current.random] if current.random else None
        result.append((current.val, random_idx))
        current = current.next

    return result


@pytest.mark.parametrize(
    "input_list, expected_list",
    [
        (
            [(7, None), (13, 0), (11, 4), (10, 2), (1, 0)],
            [(7, None), (13, 0), (11, 4), (10, 2), (1, 0)],
        ),
        ([(1, 1), (2, 1)], [(1, 1), (2, 1)]),
        ([], []),
        ([(1, None)], [(1, None)]),
        ([(3, None), (3, 0), (3, None)], [(3, None), (3, 0), (3, None)]),
    ],
)
def test_copyRandomList(input_list, expected_list):
    solution = Solution()
    head = list_to_linked_list_with_random(input_list)
    copied_head = solution.copyRandomList(head)
    result = linked_list_with_random_to_list(copied_head)
    assert result == expected_list
