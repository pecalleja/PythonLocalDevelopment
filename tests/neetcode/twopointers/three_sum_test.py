import pytest

from src.neetcode.twopointers.three_sum import Solution


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]]),
        ([0, 1, 1], []),
        ([0, 0, 0, 0], [[0, 0, 0]]),
        ([-2, 0, 1, 1, 2], [[-2, 0, 2], [-2, 1, 1]]),
        ([], []),
        ([0], []),
        ([1, 2, -2, -1], []),
    ],
)
def test_threeSum(nums, expected):
    sol = Solution()
    result = sol.threeSum(nums)

    def sort_triplets(triplets):
        return sorted([sorted(triplet) for triplet in triplets])

    assert sort_triplets(result) == sort_triplets(expected)
