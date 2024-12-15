import pytest

from src.codesignal.trees.valid_tree import solution


@pytest.mark.parametrize(
    "tree_data, expected",
    [
        ([2, 1, 3], True),
        ([1, 2, 3], False),
        ([8, 3, 10, 1, 6, None, 14], True),
        ([10, 5, 15, None, None, 6, 20], False),
        ([30, 20, 40, 10, 25], True),
        ([-1], True),
        ([], True),
        ([20, 10, 30, 5, 15], True),
        ([3, 1, 5, None, None, 4, 6], True),
        ([3, 1, 4, None, None, 5], False),
    ],
)
def test_is_binary_search_tree(list_to_tree, tree_data, expected):
    root = list_to_tree(tree_data)
    assert solution(root) == expected
