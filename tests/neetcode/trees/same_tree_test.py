import pytest

from src.neetcode.trees.same_tree import Solution


@pytest.mark.parametrize(
    "p_list, q_list, expected",
    [
        ([1, 2, 3], [1, 2, 3], True),
        ([1, 2], [1, None, 2], False),
        ([1, 2, 1], [1, 1, 2], False),
        ([], [], True),
        ([1], [1], True),
        ([1, 2, 3], [1, 2], False),  # One tree is shorter
        ([1, None, 2], [1, None, 2], True),
        ([1, 2], [1, None, None], False),
    ],
)
def test_isSameTree(list_to_tree, p_list, q_list, expected):
    solution = Solution()

    # Build trees p and q from lists
    p = list_to_tree(p_list)
    q = list_to_tree(q_list)

    # Test the isSameTree function
    result = solution.isSameTree(p, q)

    # Assert the result is as expected
    assert result == expected
