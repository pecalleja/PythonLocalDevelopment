import pytest

from src.neetcode.trees.symmetric_tree import Solution


@pytest.mark.parametrize(
    "lst, expected",
    [
        ([1, 2, 2, 3, 4, 4, 3], True),
        ([1, 2, 2, None, 3, None, 3], False),
        ([1], True),
        ([1, 2, 2, None, None, None, None], True),
        ([1, 2, 2, 3, None, None, 3], True),
        ([], True),
        ([1, 2, 2, 3, None, None, 4], False),
    ],
)
def test_isSymmetric(list_to_tree, lst, expected):
    solution = Solution()
    root = list_to_tree(lst)
    result = solution.isSymmetric(root)
    assert result == expected
