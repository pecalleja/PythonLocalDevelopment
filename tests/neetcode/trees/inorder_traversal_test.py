import pytest

from src.neetcode.trees.inorder_traversal import Solution


@pytest.mark.parametrize(
    "lst, expected",
    [
        ([1, None, 2, 3], [1, 3, 2]),
        ([], []),
        ([1], [1]),
        ([1, 2, 3, None, None, 4, 5], [2, 1, 4, 3, 5]),
        ([4, 2, 6, 1, 3, 5, 7], [1, 2, 3, 4, 5, 6, 7]),
        ([1, None, 2], [1, 2]),
    ],
)
def test_inorderTraversal(list_to_tree, lst, expected):
    solution = Solution()
    root = list_to_tree(lst)
    result = solution.inorderTraversal(root)
    assert result == expected
