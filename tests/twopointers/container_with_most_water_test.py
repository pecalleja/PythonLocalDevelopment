import pytest

from src.twopointers.container_with_most_water import Solution


@pytest.mark.parametrize(
    "height, expected",
    [
        ([1, 8, 6, 2, 5, 4, 8, 3, 7], 49),
        ([1, 1], 1),
        ([4, 3, 2, 1, 4], 16),
        ([1, 2, 1], 2),
        ([2, 3, 10, 5, 7, 8, 9], 36),
        ([1], 0),
        ([], 0),
    ],
)
def test_maxArea(height, expected):
    sol = Solution()
    assert sol.maxArea(height) == expected
