"""
Swapping Odd and Even Bits

You are provided with an integer number n, and your task is to swap every pair
of odd and even bits of this number. Bit positions are numbered from 1 to n
from right to left (or least significant to most significant). This means bit
1 (the least significant bit) should be swapped with bit 2, bit 3 should be
swapped with bit 4, and so forth.

For example, if n = 23, its binary representation is 010111. After swapping
the odd and even bits, we get 101011, which is the binary representation of 43.
So, the function swap_bits(23) will return 43.

You can only use bit manipulation in this task, type conversion is not allowed.
The expected time complexity for this task is O(log n).
"""


def solution(n):
    # Mask for bits in positions 1, 3, 5, ... (1-indexed)
    odd_mask = 0x55555555  # In binary: ...0101010101
    # Mask for bits in positions 2, 4, 6, ... (1-indexed)
    even_mask = 0xAAAAAAAA  # In binary: ...1010101010

    # Extract odd and even bits using bitwise AND.
    odd_bits = n & odd_mask
    even_bits = n & even_mask

    # Shift odd bits left to move them into even bit positions.
    # Shift even bits right to move them into odd bit positions.
    return (odd_bits << 1) | (even_bits >> 1)
