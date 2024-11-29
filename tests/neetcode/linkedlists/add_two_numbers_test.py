import pytest

from src.neetcode.linkedlists.add_two_numbers import Solution


@pytest.mark.parametrize(
    "l1, l2, expected",
    [
        ([2, 4, 3], [5, 6, 4], [7, 0, 8]),
        ([0], [0], [0]),
        ([9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9], [8, 9, 9, 9, 0, 0, 0, 1]),
        ([1, 8], [0], [1, 8]),
        ([5], [5], [0, 1]),
    ],
)
def test_add_two_numbers(
    list_to_linkedlist, linkedlist_to_list, l1, l2, expected
):
    l1_list = list_to_linkedlist(l1)
    l2_list = list_to_linkedlist(l2)
    solution = Solution()
    result = solution.addTwoNumbers(l1_list, l2_list)
    assert linkedlist_to_list(result) == expected
