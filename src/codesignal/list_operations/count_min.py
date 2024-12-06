"""
Counting the Smallest Number in an Array

You are given an array of integers. Your task is to write a function in Python
that returns the number of times the smallest element appears in the array.

Please note that built-in methods such as min() or count() should not be used
in this task. Your goal is to accomplish this task by iterating over the array
elements manually. Try to solve the task by doing just a single list traversal.
"""


def solution(numbers):
    smallest_number = float("inf")
    smallest_counter = 0
    for number in numbers:
        if number < smallest_number:
            smallest_number = number
            smallest_counter = 1
        elif smallest_number == number:
            smallest_counter += 1
    return smallest_counter
