"""
Perfect Squares Summation Minimal Count

You are given a positive integer n. Your task is to find the minimal number of
perfect squares that sum up to n. A perfect square is an integer that is the
square of some other integer. For example, 1, 4, 9, and 16 are perfect squares,
 but 2 and 3 are not. It is allowed to use the same perfect square multiple
 times.

For instance, given n equals 13, return 2 because 13 can be expressed as
4 (2⋅2) + 9 (3⋅3); therefore, the function should return 2 (the number of
 perfect squares that sum to 13).

The expected time complexity for this algorithm is O(n⋅sqrt(n)).
"""


def solution(n):
    min_squares = [0] * (n + 1)
    for i in range(1, n + 1):
        min_squares[i] = i
        for j in range(1, int(i**0.5) + 1):
            min_squares[i] = min(min_squares[i], min_squares[i - j * j] + 1)
    return min_squares[n]
