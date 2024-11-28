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
def test_preorderTraversal(build_tree_from_list, values, expected):
    sol = Solution()
    root = build_tree_from_list(values)
    assert sol.preorderTraversal(root) == expected
