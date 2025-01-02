import pytest

from src.neetcode.trees.binary_tree_maximum_path_sum import Solution


@pytest.mark.parametrize(
    "tree_list, expected",
    [
        ([1, 2, 3], 6),
        ([-10, 9, 20, None, None, 15, 7], 42),
        ([2, -1], 2),
        ([1, -2, 3], 4),
        ([1], 1),
        ([], float('-inf')),
    ],
)
def test_max_path_sum(list_to_tree, tree_list, expected):
    root = list_to_tree(tree_list)
    solution = Solution()
    assert solution.maxPathSum(root) == expected
