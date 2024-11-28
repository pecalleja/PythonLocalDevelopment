import pytest

from src.neetcode.arrays.climbing_stairs import Solution


# fmt: off
@pytest.mark.parametrize("n, expected", [
    (1, 1),          # Only 1 way to climb 1 step: [1]
    (2, 2),          # Two ways to climb 2 steps: [1+1], [2]
    (3, 3),          # Three ways to climb 3 steps: [1+1+1], [1+2], [2+1]
    (4, 5),          # Five ways to climb 4 steps
    (5, 8),          # Eight ways to climb 5 steps
    (6, 13),         # Thirteen ways to climb 6 steps
    (10, 89),        # Testing for a larger n: 89 ways to climb 10 steps
    (20, 10946),     # Testing for a larger n: 10946 ways to climb 20 steps
    (30, 1346269),   # Large test case: 1,346,269 ways to climb 30 steps
    (50, 20365011074)  # Large test case: 20,365,011,074 ways to climb 50 steps
])
# fmt: on
def test_climb_stairs(n, expected):
    assert Solution().climbStairs(n) == expected
