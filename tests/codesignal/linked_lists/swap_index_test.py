import pytest

from src.codesignal.linked_lists.swap_index import solution


# fmt: off
@pytest.mark.parametrize(
    "input_list, index1, index2, expected_output",
    [
        ([1, 2, 3, 4, 5], 0, 4, [5, 2, 3, 4, 1]),
        ([5, 4, 3, 2, 1], 1, 3, [5, 2, 3, 4, 1]),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9], 0, 8, [9, 2, 3, 4, 5, 6, 7, 8, 1]),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9], 3, 5, [1, 2, 3, 6, 5, 4, 7, 8, 9]),
        ([1, 2, 3], 0, 2, [3, 2, 1]),
        ([1, 2, 3], 1, 1, [1, 2, 3]),
        ([-9, -8, -7, -6, -5, -4, -3, -2, -1, 0], 0, 9, [0, -8, -7, -6, -5, -4, -3, -2, -1, -9]),  # noqa
        ([2], 0, 0, [2]),
        ([-5, 0, 5], 0, 2, [5, 0, -5]),
        (list(range(1, 101)), 0, 99, [100] + list(range(2, 100)) + [1]),
        (list(range(1, 101)), 50, 50, list(range(1, 101))),
    ],
)
# fmt: on
def test_swap_linked_list_nodes(
    list_to_linkedlist,
    linkedlist_to_list,
    input_list,
    index1,
    index2,
    expected_output,
):
    head = list_to_linkedlist(input_list)
    swapped_head = solution(head, index1, index2)
    assert linkedlist_to_list(swapped_head) == expected_output
