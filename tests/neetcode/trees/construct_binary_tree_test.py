import pytest

from src.neetcode.trees.construct_binary_tree import Solution


@pytest.mark.parametrize(
    "preorder, inorder, expected",
    [
        ([3, 9, 20, 15, 7], [9, 3, 15, 20, 7], [3, 9, 20, None, None, 15, 7]),
        ([-1], [-1], [-1]),
        ([1, 2], [2, 1], [1, 2]),
        ([1, 2, 3], [2, 1, 3], [1, 2, 3]),
    ],
)
def test_build_tree(tree_to_list, preorder, inorder, expected):
    solution = Solution()
    result = solution.buildTree(preorder, inorder)
    assert tree_to_list(result) == expected
