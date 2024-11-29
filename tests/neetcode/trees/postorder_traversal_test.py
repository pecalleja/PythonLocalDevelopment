import pytest

from src.neetcode.trees.postorder_traversal import Solution


@pytest.mark.parametrize(
    "values, expected",
    [
        ([1, None, 2, 3], [3, 2, 1]),
        ([], []),
        ([1], [1]),
        ([1, 2, 3], [2, 3, 1]),
        ([1, None, 2, None, 3], [3, 2, 1]),
    ],
)
def test_postorderTraversal(list_to_tree, values, expected):
    sol = Solution()
    root = list_to_tree(values)
    assert sol.postorderTraversal(root) == expected
