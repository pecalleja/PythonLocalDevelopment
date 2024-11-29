import pytest

from src.neetcode.linkedlists.merge_two_sorted_lists import Solution


@pytest.mark.parametrize(
    "list1, list2, expected",
    [
        ([1, 2, 4], [1, 3, 4], [1, 1, 2, 3, 4, 4]),
        # Example 1: Merging two sorted lists
        ([], [], []),  # Both lists are empty
        ([], [0], [0]),  # One list is empty
        ([2], [], [2]),  # One list has one element
        ([1, 3, 5], [2, 4, 6], [1, 2, 3, 4, 5, 6]),
        # Two sorted lists with alternating values
        ([5, 6, 7], [1, 2, 3], [1, 2, 3, 5, 6, 7]),
        # All elements in one list are greater than the other
        ([1, 1, 1], [2, 2, 2], [1, 1, 1, 2, 2, 2]),
        # Repeated elements in both lists
        ([1], [1], [1, 1]),  # Single element in both lists
    ],
)
def test_mergeTwoLists(
    list_to_linkedlist, linkedlist_to_list, list1, list2, expected
):
    solution = Solution()
    l1 = list_to_linkedlist(list1)
    l2 = list_to_linkedlist(list2)

    # Merge the two sorted lists
    merged_head = solution.mergeTwoLists(l1, l2)

    # Convert the merged linked list back to a Python list
    result = linkedlist_to_list(merged_head)

    # Assert the result is as expected
    assert result == expected
