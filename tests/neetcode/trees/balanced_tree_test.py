import pytest

from src.neetcode.trees.balanced_tree import Solution


@pytest.mark.parametrize(
    "lst, expected",
    [
        ([3, 9, 20, None, None, 15, 7], True),
        ([1, 2, 2, 3, 3, None, None, 4, 4], False),
        ([1], True),
        ([], True),
        ([1, 2, 2, 3, None, None, 3, 4, None, None, 4], False),
        ([1, 2, 2, 3, None, None, 3], True),
    ],
)
def test_isBalanced(build_tree_from_list, lst, expected):
    solution = Solution()
    root = build_tree_from_list(lst)
    result = solution.isBalanced(root)
    assert result == expected
