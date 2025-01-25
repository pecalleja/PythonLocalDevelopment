"""
String Patterns in Multiple Texts with KMP Algorithm

You're provided with a list of n strings and a single pattern string. Your
task is to implement a function, find_pattern_in_texts(texts, pattern),
applying the KMP String Searching Algorithm. This function will receive the
texts and the pattern as input, then return a list where each element
indicates the starting position of the first occurrence of the pattern in the
corresponding text from the texts list. If the pattern is not present in a
given text, use -1 as a placeholder.

lps = Longest Prefix Suffix
"""


def compute_lps(pattern):
    lps = [0] * len(pattern)
    length, pointer = 0, 1
    while pointer < len(pattern):
        if pattern[pointer] == pattern[length]:
            length += 1
            lps[pointer] = length
            pointer += 1
        else:
            if length == 0:
                lps[pointer] = 0
                pointer += 1
            else:
                length = lps[length - 1]
    return lps


def solution(texts, haystack):
    lps_table = compute_lps(haystack)

    def kmp_search(text, pattern):
        i = j = 0
        while i < len(text):
            if pattern[j] == text[i]:
                i += 1
                j += 1
            if j == len(pattern):
                return i - j
            elif i < len(text) and pattern[j] != text[i]:
                if j != 0:
                    j = lps_table[j - 1]
                else:
                    i += 1
        return -1

    # Apply KMP search to each text in the texts list
    return [kmp_search(text, haystack) for text in texts]
