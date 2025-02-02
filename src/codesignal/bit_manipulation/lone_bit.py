"""
Finding the Lone Set Bit Position

Implement a function find_lone_set_bit(n: int) -> int, which returns the
position of the only set bit (bit having value 1) in the binary representation
of a given non-zero integer n. If there are multiple or no set bits in the
given number, return -1.

The solution is allowed to use only bit techniques, it is not allowed to use
type conversions.

Here are some examples:
print(find_lone_set_bit(16))  # Output: 5 (16 = 10000)
print(find_lone_set_bit(13))  # Output: -1 (13 = 1101)
print(find_lone_set_bit(0))   # Output: -1 (0 = 0)

"""


def solution(n: int) -> int:
    if n == 0 or n & (n - 1) != 0:
        return -1
    position = 1
    while n > 0:
        if n & 1 == 1 and n & (n - 1) == 0:
            return position
        n >>= 1
        position += 1
    return -1
