import pytest

from src.neetcode.trees.invert_binary_tree import Solution


@pytest.mark.parametrize(
    "input_tree, expected_tree",
    [
        ([4, 2, 7, 1, 3, 6, 9], [4, 7, 2, 9, 6, 3, 1]),
        ([2, 1, 3], [2, 3, 1]),
        ([], []),  # Empty tree
        ([1], [1]),  # Single-node tree
        ([1, 2], [1, None, 2]),  # Tree with one child
    ],
)
def test_invert_tree(list_to_tree, tree_to_list, input_tree, expected_tree):
    root = list_to_tree(input_tree)
    expected = list_to_tree(expected_tree)
    solution = Solution()
    inverted = solution.invertTree(root)
    assert tree_to_list(inverted) == tree_to_list(expected)
