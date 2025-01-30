import pytest

from src.leetcode.unique_binary_tree import Solution


@pytest.mark.parametrize(
    "n, expected_lists",
    [
        (1, [[1]]),
        (2, [[1, None, 2], [2, 1]]),
        (
            3,
            [
                [1, None, 2, None, 3],
                [1, None, 3, 2],
                [2, 1, 3],
                [3, 1, None, None, 2],
                [3, 2, None, 1],
            ],
        ),
    ],
)
def test_generate_trees(n, expected_lists, tree_to_list):
    solution = Solution()
    results = solution.generateTrees(n)

    # Convert results to list representation
    result_lists = sorted([tree_to_list(tree) for tree in results])

    # Convert expected lists to sorted form
    expected_lists_sorted = sorted(expected_lists)

    assert result_lists == expected_lists_sorted, f"Failed for n={n}"
