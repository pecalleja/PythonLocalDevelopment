import pytest

from src.codesignal.linked_lists.rotate_linked_list import solution


@pytest.mark.parametrize(
    "input_list, k, expected_output",
    [
        ([1, 2, 3, 4, 5], 2, [4, 5, 1, 2, 3]),
        ([1], 0, [1]),
        ([1, 2], 1, [2, 1]),
        ([1, 2, 3], 2, [2, 3, 1]),
        ([1, 2, 3, 4], 3, [2, 3, 4, 1]),
        ([1, 2, 3, 4, 5], 4, [2, 3, 4, 5, 1]),
        ([1, 2, 3, 4, 5], 5, [1, 2, 3, 4, 5]),
        ([1, 2, 3, 4, 5], 6, [5, 1, 2, 3, 4]),
        ([1, 2, 3, 4, 5], 7, [4, 5, 1, 2, 3]),
        ([1, 2, 3, 4, 5], 1001, [5, 1, 2, 3, 4]),
        ([1], 999, [1]),
        ([1, 2], 1002, [1, 2]),
        ([1, 1, 1, 1, 2, 2, 2], 3, [2, 2, 2, 1, 1, 1, 1]),
        ([5, 5, 5, 4, 4, 4], 2, [4, 4, 5, 5, 5, 4]),
    ],
)
def test_rotate_right(
    list_to_linkedlist, linkedlist_to_list, input_list, k, expected_output
):
    head = list_to_linkedlist(input_list)
    result_head = solution(head, k)
    assert linkedlist_to_list(result_head) == expected_output
