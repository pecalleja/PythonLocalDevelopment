import pytest

from src.twopointers.trapping_rain_water import Solution


@pytest.mark.parametrize(
    "height, expected",
    [
        ([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], 6),
        ([4, 2, 0, 3, 2, 5], 9),
        ([1, 1, 1, 1], 0),
        ([0, 0, 0, 0], 0),
        ([3, 0, 2, 0, 4], 7),
        ([1], 0),
        ([], 0),
        ([0, 2, 0], 0),
        ([2, 0, 2], 2),
        ([5, 4, 1, 2], 1),
    ],
)
def test_trap(height, expected):
    sol = Solution()
    assert sol.trap(height) == expected
