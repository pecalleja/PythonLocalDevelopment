import pytest

from src.neetcode.stacks.daily_temperatures import Solution


@pytest.mark.parametrize(
    "temperatures, expected",
    [
        ([73, 74, 75, 71, 69, 72, 76, 73], [1, 1, 4, 2, 1, 1, 0, 0]),
        ([30, 40, 50, 60], [1, 1, 1, 0]),
        ([30, 60, 90], [1, 1, 0]),
        ([90, 80, 70, 60], [0, 0, 0, 0]),
        ([50], [0]),
        ([], []),
        ([70, 70, 70, 70], [0, 0, 0, 0]),
    ],
)
def test_dailyTemperatures(temperatures, expected):
    sol = Solution()
    result = sol.dailyTemperatures(temperatures)
    assert result == expected
