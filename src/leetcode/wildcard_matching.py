"""
https://leetcode.com/problems/wildcard-matching/description/

44. Wildcard Matching

Given an input string (s) and a pattern (p), implement wildcard pattern
matching with support for '?' and '*' where:

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).
The matching should cover the entire input string (not partial).

"""


class Solution:
    def isMatch(self, text: str, pattern: str) -> bool:
        text_length = len(text)
        pattern_length = len(pattern)
        match_matrix = [
            [False] * (pattern_length + 1) for _ in range(text_length + 1)
        ]
        match_matrix[0][0] = True

        for pattern_index in range(1, pattern_length + 1):
            if pattern[pattern_index - 1] == '*':
                match_matrix[0][pattern_index] = match_matrix[0][
                    pattern_index - 1
                ]

        for text_index in range(1, text_length + 1):
            for pattern_index in range(1, pattern_length + 1):
                if pattern[pattern_index - 1] == '*':
                    match_matrix[text_index][pattern_index] = (
                        match_matrix[text_index][pattern_index - 1]
                        or match_matrix[text_index - 1][pattern_index]
                    )
                elif (
                    pattern[pattern_index - 1] == '?'
                    or text[text_index - 1] == pattern[pattern_index - 1]
                ):
                    match_matrix[text_index][pattern_index] = match_matrix[
                        text_index - 1
                    ][pattern_index - 1]

        return match_matrix[text_length][pattern_length]
