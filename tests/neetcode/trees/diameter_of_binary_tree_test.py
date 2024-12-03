import pytest

from src.neetcode.trees.diameter_of_binary_tree import Solution


@pytest.mark.parametrize(
    "input_tree, expected_diameter",
    [
        ([1, 2, 3, 4, 5], 3),  # Tree with left and right subtrees
        ([1, 2], 1),  # Simple two-node tree
        ([1], 0),  # Single-node tree
        ([], 0),  # Empty tree
        ([1, 2, 3, 4, 5, 6], 4),  # Unbalanced tree
    ],
)
def test_diameter_of_binary_tree(list_to_tree, input_tree, expected_diameter):
    root = list_to_tree(input_tree)
    solution = Solution()
    assert solution.diameterOfBinaryTree(root) == expected_diameter
