import pytest

from src.neetcode.trees.minimum_depth import Solution


@pytest.mark.parametrize(
    "lst, expected",
    [
        ([3, 9, 20, None, None, 15, 7], 2),
        ([2, None, 3, None, 4, None, 5, None, 6], 5),
        ([1], 1),
        ([], 0),
        ([1, 2, 3, 4, 5], 2),
        ([1, 2], 2),
    ],
)
def test_minDepth(build_tree_from_list, lst, expected):
    solution = Solution()

    # Build tree from list
    root = build_tree_from_list(lst)

    # Test the minDepth function
    result = solution.minDepth(root)

    # Assert the result is as expected
    assert result == expected
