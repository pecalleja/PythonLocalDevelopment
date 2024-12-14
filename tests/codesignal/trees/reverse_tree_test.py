import pytest

from src.codesignal.trees.reverse_tree import solution


def inorder_traversal(root):
    return (
        inorder_traversal(root.left)
        + [root.val]
        + inorder_traversal(root.right)
        if root
        else []
    )


@pytest.mark.parametrize(
    "input_tree, expected_inorder",
    [
        ([1, 2, 5, 3, 4], [5, 1, 4, 2, 3]),
        ([7, 3, 5, 2, 6, 9], [5, 9, 7, 6, 3, 2]),
        ([1], [1]),
        ([3, 9], [3, 9]),
        ([-7, -8, -5], [-5, -7, -8]),
        ([0], [0]),
        ([4, None, 2, None, 1], [1, 2, 4]),
        (
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
            [15, 7, 14, 3, 13, 6, 12, 1, 11, 5, 10, 2, 9, 4, 8],
        ),
        (
            [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
            [1, 9, 2, 13, 3, 10, 4, 15, 5, 11, 6, 14, 7, 12, 8],
        ),
    ],
)
def test_reverse_tree(
    list_to_tree, tree_to_list, input_tree, expected_inorder
):
    tree = list_to_tree(input_tree)
    reversed_tree = solution(tree)
    assert inorder_traversal(reversed_tree) == expected_inorder
