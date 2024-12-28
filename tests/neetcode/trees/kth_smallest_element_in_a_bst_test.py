import pytest

from src.neetcode.trees.kth_smallest_element_in_a_bst import Solution


@pytest.mark.parametrize(
    "nodes, k, expected",
    [
        ([3, 1, 4, None, 2], 1, 1),
        ([5, 3, 6, 2, 4, None, None, 1], 3, 3),
        ([2, 1, 3], 2, 2),
        ([1, None, 2], 2, 2),
        ([3, 1, 4, None, 2], 2, 2),
    ],
)
def test_kth_smallest(list_to_tree, nodes, k, expected):
    root = list_to_tree(nodes)
    assert Solution().kthSmallest(root, k) == expected
