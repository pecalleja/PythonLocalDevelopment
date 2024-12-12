import pytest

from src.neetcode.trees.levelorder_traversal import Solution


@pytest.mark.parametrize(
    "tree_list, expected",
    [
        ([3, 9, 20, None, None, 15, 7], [[3], [9, 20], [15, 7]]),
        ([1], [[1]]),  # Single-node tree
        ([], []),  # Empty tree
        ([1, 2, 3, 4, 5], [[1], [2, 3], [4, 5]]),  # Full binary tree
        ([1, None, 2, None, 3], [[1], [2], [3]]),  # Skewed tree (right)
        ([1, 2, None, 3], [[1], [2], [3]]),  # Skewed tree (left)
    ],
)
def test_level_order(list_to_tree, tree_list, expected):
    root = list_to_tree(tree_list)
    solution = Solution()
    assert solution.levelOrder(root) == expected
