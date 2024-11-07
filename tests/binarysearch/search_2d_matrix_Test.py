import pytest

from src.binarysearch.search_2d_matrix import Solution


@pytest.mark.parametrize(
    "matrix, target, expected",
    [
        ([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3, True),
        ([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13, False),
        ([[1]], 1, True),
        ([[1]], 2, False),
        ([], 1, False),
        ([[1, 2, 3, 4], [5, 6, 7, 8]], 8, True),
        ([[1, 2, 3, 4], [5, 6, 7, 8]], 0, False),
        ([[1, 2, 3, 4], [5, 6, 7, 8]], 10, False),
        ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 5, True),
        ([[10, 20, 30], [40, 50, 60], [70, 80, 90]], 45, False),
    ],
)
def test_searchMatrix(matrix, target, expected):
    sol = Solution()
    assert sol.searchMatrix(matrix, target) == expected
