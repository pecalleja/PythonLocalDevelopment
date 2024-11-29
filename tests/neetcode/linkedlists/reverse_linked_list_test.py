import pytest

from src.neetcode.linkedlists.reverse_linked_list import Solution


@pytest.mark.parametrize(
    "input_list, expected_list",
    [
        ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]),  # Regular case
        ([1, 2], [2, 1]),  # Short list
        ([1], [1]),  # Single element
        ([], []),  # Empty list
        ([1, 2, 2, 1], [1, 2, 2, 1]),  # Palindromic list
    ],
)
def test_reverseList(
    list_to_linkedlist, linkedlist_to_list, input_list, expected_list
):
    sol = Solution()
    head = list_to_linkedlist(input_list)
    reversed_head = sol.reverseList(head)
    result_list = linkedlist_to_list(reversed_head)
    assert result_list == expected_list
