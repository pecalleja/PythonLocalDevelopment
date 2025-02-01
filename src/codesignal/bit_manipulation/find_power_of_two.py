"""
Check If Number Is Power Of Two Using Bit Manipulation Techniques

You are provided with a positive integer. Your task is to write a function
find_power_of_two(n) that returns True if the number n is a power of 2 and
False otherwise. You are to solve this problem using only bit manipulation
techniques, it is not allowed to use type conversions.

The expected time complexity is O(1).

For a number that is a power of two, its binary representation has exactly one
bit set to 1
(e.g., 1 is 0001, 2 is 0010, 4 is 0100, etc.).

Subtracting 1 from such a number of flips all the bits after the rightmost
1 bit, including the 1 bit itself
(e.g., 4 is 0100, and 4 - 1 is 3 which is 0011).

Performing a bitwise AND operation between the number and the number minus one
will result in 0 if the number is a power of two
(e.g., 4 & 3 is 0100 & 0011 which is 0000).
"""


def solution(n):
    return n > 0 and (n & (n - 1)) == 0
