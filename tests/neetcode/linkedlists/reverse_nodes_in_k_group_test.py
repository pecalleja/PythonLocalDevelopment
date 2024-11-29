import pytest

from src.neetcode.linkedlists.reverse_nodes_in_k_group import Solution


@pytest.mark.parametrize(
    "elements, k, expected",
    [
        ([1, 2, 3, 4, 5], 2, [2, 1, 4, 3, 5]),
        ([1, 2, 3, 4, 5], 3, [3, 2, 1, 4, 5]),
        ([1], 1, [1]),  # Single node
        ([1, 2], 3, [1, 2]),  # Group size larger than the list
        ([], 2, []),  # Empty list
    ],
)
def test_reverse_k_group(
    list_to_linkedlist, linkedlist_to_list, elements, k, expected
):
    solution = Solution()
    head = list_to_linkedlist(elements)
    result = solution.reverseKGroup(head, k)
    assert linkedlist_to_list(result) == expected
