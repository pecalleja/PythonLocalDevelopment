import pytest

from src.arrays.top_k_frequent_elements import Solution


@pytest.mark.parametrize(
    "nums, k, expected",
    [
        ([1, 1, 1, 2, 2, 3], 2, [1, 2]),
        # Example 1: 1 occurs 3 times, 2 occurs 2 times
        ([1], 1, [1]),  # Single element in the list
        ([4, 4, 1, 1, 2, 2, 3], 3, [1, 2, 4]),  # Top 3 most frequent elements
        ([1, 1, 2, 2, 3, 3], 2, [1, 2]),
        # All numbers have the same frequency, any top 2 are valid
        ([1, 2, 3, 4, 5, 6], 3, [1, 2, 3]),
        # Each element has the same frequency (all 1), top k are the first 3
        ([1, 2, 3, 3, 4, 4, 4, 5, 5, 5, 5], 2, [5, 4]),
        # Numbers 5 and 4 are the most frequent
        ([-1, -1, -2, -2, -3], 2, [-1, -2]),
        # Negative numbers with the top 2 most frequent
        ([0, 0, 0, 1, 1, 2, 2, 2, 2, 3], 1, [2]),  # Most frequent number is 2
    ],
)
def test_topKFrequent(nums, k, expected):
    solution = Solution()
    result = solution.topKFrequent(nums, k)
    assert sorted(result) == sorted(expected)
