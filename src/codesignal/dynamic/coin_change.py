"""
Dynamic Programming: Coin Change Problem

In this task, your goal is to find the number of distinct ways you can make
change for a target amount, given an array of available coin denominations.
Specifically, you need to write a Python function coin_change
(coins: List[int], amount: int) -> int, where:

coins is a list of integers representing the available denominations. Each
denomination can be used an unlimited number of times. This array contains
unique numbers.
amount is a non-negative integer representing the target amount.
The function should return an integer — the number of distinct ways you can c
ombine the coins to sum up to the target amount. If there is no possible
combination that would result in the target amount, return 0.

The expected time complexity of your solution is O(amount×len(coins).
"""


def solution(coins, amount):
    # Create a list to store the number of ways to make change for each amount
    dp = [0] * (amount + 1)
    dp[0] = 1

    # Iterate through the coins
    for coin in coins:
        # For each coin, iterate through the amounts
        for i in range(coin, amount + 1):
            # Update the number of ways to make change
            dp[i] += dp[i - coin]

    # Return the number of ways to make change for the target amount
    return dp[amount]
