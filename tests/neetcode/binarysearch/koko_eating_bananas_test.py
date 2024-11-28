import pytest

from src.neetcode.binarysearch.koko_eating_bananas import Solution


@pytest.mark.parametrize(
    "piles, h, expected",
    [
        ([3, 6, 7, 11], 8, 4),
        ([30, 11, 23, 4, 20], 5, 30),
        ([30, 11, 23, 4, 20], 6, 23),
        ([1, 1, 1, 1, 1], 5, 1),
        ([1], 1, 1),
        ([1000], 1, 1000),
        ([10, 10, 10, 10], 10, 5),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9], 9, 9),
        ([5, 10, 15, 20], 7, 10),
        ([312884470], 968709470, 1),
    ],
)
def test_minEatingSpeed(piles, h, expected):
    sol = Solution()
    assert sol.minEatingSpeed(piles, h) == expected
