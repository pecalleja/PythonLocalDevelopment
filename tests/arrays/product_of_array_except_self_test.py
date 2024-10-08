import pytest

from src.arrays.product_of_array_except_self import Solution


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([1, 2, 3, 4], [24, 12, 8, 6]),
        ([5, 6, 2, 3], [36, 30, 90, 60]),
        ([2, 3], [3, 2]),
        ([1, 0], [0, 1]),
        ([0, 0], [0, 0]),
        ([9, 0, 2], [0, 18, 0]),
        ([1, 2, 3, 0, 5], [0, 0, 0, 30, 0]),
        ([1, 2, 0, 4], [0, 0, 8, 0]),
        ([1, 1, 1, 1], [1, 1, 1, 1]),
        ([1, 2, 3, 4, 5], [120, 60, 40, 30, 24]),
    ],
)
def test_productExceptSelf(nums, expected):
    solution = Solution()
    result = solution.productExceptSelf(nums)

    # Assert that the result matches the expected output
    assert result == expected
