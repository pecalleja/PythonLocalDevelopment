import pytest

from src.neetcode.linkedlists.remove_nth_node_from_end_of_list import Solution


@pytest.mark.parametrize(
    "input_list, n, expected_list",
    [
        ([1, 2, 3, 4, 5], 2, [1, 2, 3, 5]),
        ([1], 1, []),
        ([1, 2], 1, [1]),
        ([1, 2], 2, [2]),
        ([1, 2, 3], 3, [2, 3]),
        ([1, 2, 3, 4, 5, 6], 3, [1, 2, 3, 5, 6]),
    ],
)
def test_removeNthFromEnd(
    list_to_linkedlist, linkedlist_to_list, input_list, n, expected_list
):
    solution = Solution()
    head = list_to_linkedlist(input_list)
    updated_head = solution.removeNthFromEnd(head, n)
    result = linkedlist_to_list(updated_head)
    assert result == expected_list
