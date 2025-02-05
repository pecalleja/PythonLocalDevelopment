"""
Counting the Number of Different Bits Between Two Integers

You are to write a function get_bit_diff(a, b) that calculates the count of
different bits between two integers a and b. This function should return an
integer representing the number of positions at which the corresponding bits
are different.

For example, if a = 14 (1110) and b = 15 (1111), the
function get_bit_diff(a, b) should return 1, as it is only one bit different
in the binary representation of a and b.

You can only use bit manipulation in this task, type conversion is not allowed.
"""


def solution(a, b):
    # XOR the two numbers to find differing bits
    xor_result = a ^ b

    # Count the number of 1s in the XOR result
    count = 0
    while xor_result:
        count += xor_result & 1
        xor_result >>= 1

    return count
