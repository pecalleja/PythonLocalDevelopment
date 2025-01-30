"""
Counting Palindromic Substrings of a Given Length

You are given a text string and a number length. Your task is to count the
number of substrings of exactly length characters in the string that are
palindromes.
A string is a palindrome if it reads the same backward as forward.
Function signature: count_palindromes(text: str, length: int) -> int
For instance,
text = "madamargentinamanitnegra"
length = 5
print(count_palindromes(text, length)) # Output: 2
should return 2 because there are three substrings of length 5 that are
palindromes: madam, and naman.

The expected time complexity for this task is linear, which is O(text.length).
"""


def solution(text: str, length: int) -> int:
    if length > len(text):
        return 0

    count = 0
    # Sliding window across the text
    for i in range(len(text) - length + 1):
        substring = text[i:i+length]
        if substring == substring[::-1]:  # Check if it's a palindrome
            count += 1
    return count
