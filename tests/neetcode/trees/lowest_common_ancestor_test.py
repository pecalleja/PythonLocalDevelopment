from typing import Optional

import pytest

from src.common import TreeNode
from src.neetcode.trees.lowest_common_ancestor import Solution


def find_node(root: TreeNode, value: int) -> Optional[TreeNode]:
    """Helper function to find a node with given value in the tree"""
    if not root:
        return None
    if root.val == value:
        return root
    if value < root.val:
        return find_node(root.left, value)
    return find_node(root.right, value)


@pytest.mark.parametrize(
    "tree_values, p_val, q_val, expected_lca",
    [
        ([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5], 2, 8, 6),
        ([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5], 2, 4, 2),
        ([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5], 7, 9, 8),
        ([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5], 2, 3, 2),
        ([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5], 7, 9, 8),
        ([2, 1], 2, 1, 2),
        ([1], 1, 1, 1),
    ],
)
def test_lowest_common_ancestor(
    list_to_tree, tree_values, p_val, q_val, expected_lca
):
    solution = Solution()
    root = list_to_tree(tree_values)
    p_node = find_node(root, p_val)
    q_node = find_node(root, q_val)
    result = solution.lowestCommonAncestor(root, p_node, q_node)
    assert result.val == expected_lca
