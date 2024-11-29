import pytest

from src.neetcode.trees.preorder_traversal import Solution


@pytest.mark.parametrize(
    "values, expected",
    [
        ([1, None, 2, 3], [1, 2, 3]),
        ([], []),
        ([1], [1]),
        ([1, 2, 3], [1, 2, 3]),
        ([1, None, 2, None, 3], [1, 2, 3]),
    ],
)
def test_preorderTraversal(list_to_tree, values, expected):
    sol = Solution()
    root = list_to_tree(values)
    assert sol.preorderTraversal(root) == expected
