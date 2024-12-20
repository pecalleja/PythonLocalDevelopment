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
    # Create a list to store the number of perfect squares that sum up to each
    # number from 0 to n
    dp = [0] * (n + 1)

    # Iterate through the numbers from 1 to n
    for i in range(1, n + 1):
        # Initialize the minimum number of perfect squares to the maximum
        # possible value
        dp[i] = i

        # Iterate through the perfect squares less than or equal to i
        for j in range(1, int(i**0.5) + 1):
            # Update the minimum number of perfect squares
            dp[i] = min(dp[i], dp[i - j * j] + 1)

    # Return the minimum number of perfect squares that sum up to n
    return dp[n]
