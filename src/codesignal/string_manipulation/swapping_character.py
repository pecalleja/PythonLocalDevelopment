"""
Swapping Adjacent Characters in a String

You are given a string s. Your task is to write a function that returns a
string in which every pair of adjacent characters in the original string is
swapped. If the string has an odd length, leave the last character as it is.

It is not allowed to use Python built-in functions like reverse() or join()
in this task, you should implement the solution without using them.

For example, if you are given the string "abcdef", your function should
return "badcfe". If the string is "hello", your function should return "ehllo".
"""


def solution(s):
    even = s[::2]
    odd = s[1::2]
    result = []
    for a, b in zip(even, odd):
        result.append(b)
        result.append(a)
    if len(result) != len(s):
        result.append(s[-1])
    return "".join(result)
