import pytest

from src.stacks.car_fleet import Solution


@pytest.mark.parametrize(
    "target, position, speed, expected",
    [
        (12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3], 3),  # Case 1
        (10, [3], [3], 1),  # Case 2
        (100, [0, 2, 4], [4, 2, 1], 1),  # Case 3
    ],
)
def test_carFleet(target, position, speed, expected):
    solution = Solution()
    assert solution.carFleet(target, position, speed) == expected
