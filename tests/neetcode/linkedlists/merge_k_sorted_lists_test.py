import pytest

from src.neetcode.linkedlists.merge_k_sorted_lists import Solution


@pytest.mark.parametrize(
    "input_lists, expected",
    [
        ([[1, 4, 5], [1, 3, 4], [2, 6]], [1, 1, 2, 3, 4, 4, 5, 6]),
        ([], []),
        ([[]], []),
        ([[1], [0]], [0, 1]),
    ],
)
def test_merge_k_sorted_lists(
    linked_list_to_list, build_linked_list, input_lists, expected
):
    # Convert input lists to linked lists
    linked_lists = [build_linked_list(elements) for elements in input_lists]

    # Run the solution
    solution = Solution()
    result = solution.mergeKLists(linked_lists)

    # Convert result linked list back to a list
    result_list = linked_list_to_list(result)

    assert result_list == expected
