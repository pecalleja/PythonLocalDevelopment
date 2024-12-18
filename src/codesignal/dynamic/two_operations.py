"""
Minimum Steps to Reach Target using Dynamic Programming

Given a number, you can perform only two types of operations with it:
Add 1
Multiply by 2
Write a function min_steps(n) that takes an integer n and computes the minimum
number of steps required to transform the number 0 into the number n.

You should solve this task with O(n) time complexity using dynamic programming.

For example, min_steps(8) = 4, because:

Start from 0
Add 1 to get 1 (1 step)
Multiply by 2 to get 2 (1 step)
Multiply by 2 again to get 4 (1 step)
Multiply by 2 one more time to get 8 (1 step)
"""


def min_steps(n):
    steps = [0] * (n + 1)
    for i in range(1, n + 1):
        steps[i] = steps[i - 1] + 1
        if i % 2 == 0:
            steps[i] = min(steps[i], steps[i // 2] + 1)
    return steps[n]
