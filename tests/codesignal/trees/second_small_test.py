import pytest

from src.codesignal.trees.second_small import solution


@pytest.mark.parametrize(
    "lst, expected",
    [
        ([2, 1, 3], 2),
        ([1, 1, 1], None),
        ([1, None, 2], 2),
        ([2, 1, None], 2),
        ([0, None, -1], 0),
        ([-(10**9), 10**9], 10**9),
        ([2], None),
        ([3, 2, None, 1], 2),
    ],
)
def test_second_minimum_in_tree(list_to_tree, lst, expected):
    root = list_to_tree(lst)
    assert solution(root) == expected
