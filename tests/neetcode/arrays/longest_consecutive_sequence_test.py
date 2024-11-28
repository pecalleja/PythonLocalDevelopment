import pytest

from src.neetcode.arrays.longest_consecutive_sequence import Solution


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([100, 4, 200, 1, 3, 2], 4),
        ([0, 3, 7, 2, 5, 8, 4, 6, 0, 1], 9),
        ([], 0),
        ([1], 1),
        ([9, 1, -1, 0], 3),
        ([10, 5, 6, 4, 20, 11], 3),
        ([5, 5, 5, 5], 1),
        ([100, 101, 102, 1, 2, 3, 4, 5, 6], 6),
        ([1, 9, 3, 10, 2, 20], 3),
    ],
)
def test_longestConsecutive(nums, expected):
    solution = Solution()
    result = solution.longestConsecutive(nums)

    # Assert that the result matches the expected output
    assert result == expected
