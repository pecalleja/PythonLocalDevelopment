import pytest

from src.codesignal.bit_manipulation.swap_bits import solution


@pytest.mark.parametrize(
    "n, expected",
    [
        (23, 43),  # 23 in binary is 010111, after swapping we get 101011 (43)
        (2, 1),  # 2: binary 10 -> swapped to 01 (1)
        (1, 2),  # 1: binary 01 -> swapped to 10 (2)
        (0, 0),  # 0 remains 0 after swapping
        (100, 152),  # 100: binary 01100100 -> swapped becomes 10011000 (152)
    ],
)
def test_swap_bits(n, expected):
    assert solution(n) == expected
