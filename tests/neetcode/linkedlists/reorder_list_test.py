import pytest

from src.neetcode.linkedlists.reorder_list import Solution


@pytest.mark.parametrize(
    "input_list, expected_list",
    [
        ([1, 2, 3, 4], [1, 4, 2, 3]),
        ([1, 2, 3, 4, 5], [1, 5, 2, 4, 3]),
        ([1], [1]),
        ([1, 2], [1, 2]),
        ([], []),
        ([1, 2, 3, 4, 5, 6], [1, 6, 2, 5, 3, 4]),
    ],
)
def test_reorderList(
    linked_list_to_list, build_linked_list, input_list, expected_list
):
    solution = Solution()
    head = build_linked_list(input_list)
    solution.reorderList(head)
    result = linked_list_to_list(head)
    assert result == expected_list
