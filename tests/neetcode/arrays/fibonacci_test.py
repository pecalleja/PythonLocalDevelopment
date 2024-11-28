import pytest

from src.neetcode.arrays.fibonacci import Solution


@pytest.mark.parametrize(
    "n, expected",
    [
        (0, 0),  # Base case: F(0) = 0
        (1, 1),  # Base case: F(1) = 1
        (2, 1),  # F(2) = F(1) + F(0) = 1 + 0 = 1
        (3, 2),  # F(3) = F(2) + F(1) = 1 + 1 = 2
        (4, 3),  # F(4) = F(3) + F(2) = 2 + 1 = 3
        (5, 5),  # F(5) = F(4) + F(3) = 3 + 2 = 5
        (6, 8),  # F(6) = F(5) + F(4) = 5 + 3 = 8
        (10, 55),  # Testing for a higher n: F(10) = 55
        (20, 6765),  # Testing for a larger n: F(20)
        (30, 832040),  # Larger test case: F(30)
        (50, 12586269025),  # Large test case: F(50)
    ],
)
def test_fib(n, expected):
    assert Solution().fib(n) == expected
