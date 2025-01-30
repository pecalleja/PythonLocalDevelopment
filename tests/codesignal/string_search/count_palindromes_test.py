import pytest

from src.codesignal.string_search.count_palindromes import solution


@pytest.mark.parametrize(
    "text, length, expected",
    [
        ("madamargentinamanitnegra", 5, 2),
        ("racecar", 7, 1),
        ("abcba", 1, 5),
        ("a", 1, 1),
        ("level", 2, 0),
        ("abcd", 2, 0),
        ("abcd", 1, 4),
        ("racecar", 3, 1),
        ("tocat", 5, 0),
        ("abcdabcdabcddcba", 4, 1),
        ("python", 2, 0),
        ("abcdabcabcabcdabc", 3, 0),
        ("abcdabcabcabcdabc", 4, 0),
        ("abcdabcabcabcdabc", 5, 0),
        ("abcdefghijklmnonmlkjihgfedcba", 5, 1),
        ("abcdefghijklmnonmlkjihgfedcba", 26, 0),
        ("abcdefghihgfedcba", 17, 1),
        ("abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd", 5, 0),
        ("abcdeedcba", 9, 0),
        ("noonxnoonxnoon", 4, 3),
        ("abaccabacca", 4, 2),
        ("aabaaabaaa", 3, 4),
        ("xyzyxyzy", 3, 3),
        ("ababababa", 5, 5),
        ("ababbbabba", 3, 4),
        ("eeeeeeee", 2, 7),
        ("racecarxeracecar", 7, 2),
        ("xanaxxyxanaxyxana", 3, 5),
        ("bbbbb", 1, 5),
        ("bbbbb", 2, 4),
        ("bbbbb", 3, 3),
    ],
)
def test_count_palindromes(text, length, expected):
    assert solution(text, length) == expected
