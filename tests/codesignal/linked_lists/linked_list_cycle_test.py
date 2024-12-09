import pytest

from src.codesignal.linked_lists.linked_list_cycle import solution


@pytest.mark.parametrize(
    "values, pos, expected_output",
    [
        ([1], None, False),
        ([1, 2, 3], None, False),
        ([1, 2, 3], 0, True),
        ([1, 2, 2, 1], None, False),
        ([1, 2, 3, 4, 5], 2, True),
        ([i for i in range(1, 100001)], 0, True),
    ],
)
def test_hasCycle(list_to_linkedlist, values, pos, expected_output):
    head = list_to_linkedlist(values, pos)
    assert solution(head) == expected_output
