import pytest

from src.neetcode.stacks.largest_rectangle import Solution


# fmt: off
@pytest.mark.parametrize("heights, expected", [
    ([2, 1, 5, 6, 2, 3], 10),    # Case 1
    ([2, 4], 4),                 # Case 2
    ([1, 1, 1, 1], 4),           # All bars have the same height
    ([6, 7, 5, 2, 4, 5, 9, 3], 16),  # Largest rectangle spans [7, 5, 2, 4]
    ([1], 1),                    # Single bar
    ([1, 2, 3, 4, 5], 9),        # Increasing heights
    ([5, 4, 3, 2, 1], 9),        # Decreasing heights
    ([], 0),                     # Empty histogram
    ([2, 2, 2, 2], 8),           # Uniform height bars
    ([2, 1, 2], 3),              # Bars in the shape of a valley
    ([4, 2, 0, 3, 2, 5], 6),     # Complex case with varying heights
])
# fmt: on
def test_largestRectangleArea(heights, expected):
    solution = Solution()
    assert solution.largestRectangleArea(heights) == expected
