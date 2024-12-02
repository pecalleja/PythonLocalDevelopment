import pytest

from src.neetcode.trees.maximum_depth import Solution


@pytest.mark.parametrize(
    "tree_array, expected",
    [
        ([1], 1),  # Single node tree
        ([], 0),  # Empty tree
        ([1, 2, None, 3], 3),  # Left-skewed tree: 1 -> 2 -> 3
        ([1, None, 2, None, 3], 3),  # Right-skewed tree: 1 -> 2 -> 3
        ([1, 2, 3, 4, 5], 3),  # Balanced tree: Depth is 3
        ([1, 2, None, 3, None, None, 4], 4),  # Unbalanced tree: Depth is 4
        ([3, 9, 20, None, None, 15, 7], 3),
        ([1, None, 2], 2),
    ],
)
def test_maxDepth(list_to_tree, tree_array, expected):
    root = list_to_tree(tree_array)
    solution = Solution()
    assert solution.maxDepth(root) == expected
