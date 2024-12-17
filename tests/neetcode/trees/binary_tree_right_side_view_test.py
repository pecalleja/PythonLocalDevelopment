import pytest

from src.neetcode.trees.binary_tree_right_side_view import Solution


@pytest.mark.parametrize(
    "tree_list, expected",
    [
        ([1, 2, 3, None, 5, None, 4], [1, 3, 4]),
        ([1, None, 3], [1, 3]),
        ([], []),
        ([1, 2, None, 4, 5, None, None, 6], [1, 2, 5, 6]),
        ([1, 2, 3, 4, 5], [1, 3, 5]),
        ([1, 2, 3, 4, None, None, None, 5], [1, 3, 4, 5]),
    ],
)
def test_right_side_view(list_to_tree, tree_list, expected):
    solution = Solution()
    tree_root = list_to_tree(tree_list)
    assert solution.rightSideView(tree_root) == expected
