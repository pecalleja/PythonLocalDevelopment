"""
Counting Unset Bits in an Integer

Your task is to write a Python function named count_unset_bits. This function
will take a 32-bit integer n as input and return the number of unset (0) bits
in the binary representation of the given number.

The solution is allowed to use only bit techniques, it is not allowed to use
type conversions.
"""


def solution(n: int) -> int:
    count = 0
    for i in range(32):
        if (n & (1 << i)) == 0:
            count += 1
    return count
