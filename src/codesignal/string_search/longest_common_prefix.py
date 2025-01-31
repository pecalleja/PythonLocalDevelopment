"""
Longest Common Prefix in a List of Strings

You are given a list of n words. All the words are in lowercase. Your task is
to design an efficient method to find the longest common prefix shared among
all the words in the list. The function should return the longest common
prefix, which is a substring of each word. If there's no common prefix, the
function should return an empty string.

The expected time complexity for your solution is O(N∗M∗logM), where N is the
number of strings in the input and M is the maximum length of a string.

For example:

longest_common_prefix([
    "flower", "flow", "flight"
])
should return "fl"

longest_common_prefix([
    "dog", "racecar", "car"
])
should return "" (an empty string means there's no common prefix)
"""


def solution(words: list[str]) -> str:
    if not words:
        return ""

    # Sort the words to bring similar prefixes together
    words.sort()

    # Compare characters of the first and last word in the sorted list
    first_word = words[0]
    last_word = words[-1]
    common_prefix = []

    for i in range(len(first_word)):
        if i >= len(last_word) or first_word[i] != last_word[i]:
            break
        common_prefix.append(first_word[i])

    return ''.join(common_prefix)
