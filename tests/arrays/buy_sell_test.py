import pytest

from src.arrays.buy_sell import Solution


@pytest.mark.parametrize(
    "prices, expected",
    [
        ([7, 1, 5, 3, 6, 4], 5),
        ([7, 6, 4, 3, 1], 0),
        ([1, 2, 3, 4, 5], 4),
        ([3, 2, 6, 5, 0, 3], 4),
        ([1], 0),
        ([2, 4, 1], 2),
    ],
)
def test_maxProfit(prices, expected):
    solution = Solution()
    assert solution.maxProfit(prices) == expected
