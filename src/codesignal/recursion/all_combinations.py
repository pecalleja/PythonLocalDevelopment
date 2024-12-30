"""
Generating All Combinations of String Characters Using Recursion

Given a string s of n characters, your task is to write a Python function
called all_combinations(s) that uses a recursive algorithm to generate and
return a list of all possible combinations of the characters in the string,
including the original string and its reverse. The combinations should be
sorted in alphabetical order.

For instance, if the input is 'abc', the function should return a list of
all possible combinations:
[
    'a', 'ab', 'abc', 'ac', 'acb', 'b', 'ba',
    'bac', 'bc', 'bca', 'c', 'ca', 'cab', 'cb', 'cba'
]
"""


def solution(s: str) -> list:
    def generate_permutations(current, remaining):
        if current:
            result.add(current)
        if not remaining:
            return
        for i in range(len(remaining)):
            char = remaining[i]
            generate_permutations(
                current + char, remaining[:i] + remaining[i+1:]  # noqa
            )

    result = set()

    for i in range(len(s)):
        result.add(s[i])
        generate_permutations(s[i], s[:i] + s[i+1:])  # noqa
    return sorted(list(result))
