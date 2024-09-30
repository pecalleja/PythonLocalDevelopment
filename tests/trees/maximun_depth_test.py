from collections import deque

import pytest

from src.trees.maximun_depth import Solution
from src.trees.maximun_depth import TreeNode


# Helper function to build a binary tree from a level-order list
def build_tree_from_list(values):
    if not values:
        return None

    root = TreeNode(values[0])
    queue = deque([root])
    i = 1

    while queue and i < len(values):
        current = queue.popleft()

        if values[i] is not None:
            current.left = TreeNode(values[i])
            queue.append(current.left)
        i += 1

        if i < len(values) and values[i] is not None:
            current.right = TreeNode(values[i])
            queue.append(current.right)
        i += 1

    return root


@pytest.mark.parametrize(
    "tree_array, expected",
    [
        ([1], 1),  # Single node tree
        ([], 0),  # Empty tree
        ([1, 2, None, 3], 3),  # Left-skewed tree: 1 -> 2 -> 3
        ([1, None, 2, None, 3], 3),  # Right-skewed tree: 1 -> 2 -> 3
        ([1, 2, 3, 4, 5], 3),  # Balanced tree: Depth is 3
        ([1, 2, None, 3, None, None, 4], 4),  # Unbalanced tree: Depth is 4
    ],
)
def test_maxDepth(tree_array, expected):
    root = build_tree_from_list(tree_array)
    solution = Solution()
    assert solution.maxDepth(root) == expected
