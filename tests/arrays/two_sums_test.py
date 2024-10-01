import pytest

from src.arrays.two_sum import Solution


# fmt: off
@pytest.mark.parametrize("nums, target, expected", [
    ([2, 7, 11, 15], 9, [0, 1]),        # Example 1: 2 and 7 add up to 9
    ([3, 2, 4], 6, [1, 2]),             # Example 2: 2 and 4 add up to 6
    ([3, 3], 6, [0, 1]),                # Example 3: 3 and 3 add up to 6
    ([1, 2, 3, 4, 5], 9, [3, 4]),       # 4 and 5 adding up to 9
    ([5, 6, 1, 2], 7, [0, 3]),          # Numbers 5 and 2 add up to 7
    ([10, 20, 30, 40], 50, [0, 3]),     # Numbers 10 and 40 add up to 50
    ([1, 2, 3, 8, 7], 10, [1, 3]),      # Numbers 2 and 8 add up to 10
    ([4, 6], 10, [0, 1]),               # Two elements that sum up to target
    ([2, 5, 5, 11], 10, [1, 2]),        # Duplicate values
    ([1, 4, 6, 8], 15, None),           # No combination found
    ([3, 2, 95, 4, -3], 92, [2, 4]),    # Includes negative numbers
])
# fmt: on
def test_twoSum(nums, target, expected):
    solution = Solution()
    assert solution.twoSum(nums, target) == expected
