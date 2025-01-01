"""
Generating Letter Case Combinations in a String

You are given a string s, your task is to implement a function that returns
all possible letter case combinations in the string.

For example, if the input string is s = "a1b2", the output should be
["a1b2", "a1B2", "A1b2", "A1B2"]. Another example: if the input string is
s = "3z4", the output should be ["3z4", "3Z4"].

Your function should handle both lowercase and uppercase input, and it should
treat digits and special characters as invariable elements.
"""


def solution(s: str) -> list:
    def backtrack(chars, pos, curr, result):
        if pos == len(chars):
            result.append(''.join(curr))
            return

        if chars[pos].isalpha():
            # Try lowercase
            curr[pos] = chars[pos].lower()
            backtrack(chars, pos + 1, curr, result)

            # Try uppercase
            curr[pos] = chars[pos].upper()
            backtrack(chars, pos + 1, curr, result)
        else:
            # Keep non-alphabetic characters unchanged
            curr[pos] = chars[pos]
            backtrack(chars, pos + 1, curr, result)

    result = []
    chars = list(s)
    backtrack(chars, 0, chars.copy(), result)
    return result
