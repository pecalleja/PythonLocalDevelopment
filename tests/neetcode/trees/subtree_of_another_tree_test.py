import pytest

from src.neetcode.trees.subtree_of_another_tree import Solution


@pytest.mark.parametrize(
    "root_vals, subroot_vals, expected",
    [
        ([3, 4, 5, 1, 2], [4, 1, 2], True),  # Subtree match
        (
            [3, 4, 5, 1, 2, None, None, None, None, 0],
            [4, 1, 2],
            False,
        ),  # Subtree doesn't match
        ([1, 1], [1], True),  # Subtree is a single node
        ([1, 2, 3], [2], True),  # Single-node subtree match
        ([1, 2, 3], [4], False),  # Single-node subtree doesn't match
    ],
)
def test_is_subtree(list_to_tree, root_vals, subroot_vals, expected):
    root = list_to_tree(root_vals)
    subroot = list_to_tree(subroot_vals)
    solution = Solution()
    assert solution.isSubtree(root, subroot) == expected
