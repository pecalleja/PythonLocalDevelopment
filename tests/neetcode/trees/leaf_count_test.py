import pytest

from src.neetcode.trees.leaf_count import Solution


@pytest.mark.parametrize(
    "lst, expected",
    [
        ([1, 2, 3, 4, 5], 3),
        ([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1], 4),
        ([1, 2, None, 3, None, 4], 1),
        ([1, 2, 3, None, None, None, None], 2),
        ([1], 1),
        ([], 0),
        ([1, 2, 3, None, 4, None, 5], 2),
    ],
)
def test_countLeaves(list_to_tree, lst, expected):
    solution = Solution()

    # Build tree from list
    root = list_to_tree(lst)

    # Test the countLeaves function
    result = solution.countLeaves(root)

    # Assert the result is as expected
    assert result == expected
