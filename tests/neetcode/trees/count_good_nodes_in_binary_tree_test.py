import pytest

from src.neetcode.trees.count_good_nodes_in_binary_tree import Solution


@pytest.mark.parametrize(
    "tree_list, expected",
    [
        ([3, 1, 4, 3, None, 1, 5], 4),
        ([1], 1),
        ([2, 2, 2], 3),
        ([9, 4, 3, None, None, 5, 7], 1),
        ([1, 2, 3, 4, 5, 6, 7], 7),
        ([1, None, 2, None, 3], 3),
        ([3, 3, None, 4, 2], 3),
        ([8, 4, 10, None, 6, 9, 12], 3),
    ],
)
def test_good_nodes(list_to_tree, tree_list, expected):
    root = list_to_tree(tree_list)
    solution = Solution()
    assert solution.goodNodes(root) == expected
