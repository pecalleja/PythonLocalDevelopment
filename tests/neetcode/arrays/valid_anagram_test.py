import pytest

from src.neetcode.arrays.valid_anagram import Solution


# fmt: off
@pytest.mark.parametrize("s, t, expected", [
    ("anagram", "nagaram", True),   # Simple valid anagram
    ("rat", "car", False),          # Not an anagram
    ("", "", True),                 # Both strings are empty
    ("a", "a", True),               # Single characters that are equal
    ("a", "b", False),              # Single characters that are not equal
    ("ab", "ba", True),             # Simple anagram with two characters
    ("abc", "bca", True),           # Three-character anagram
    ("abc", "abcd", False),         # Different lengths
    ("aaaaa", "aaaaa", True),       # Same character repeated
    ("listen", "silent", True),     # Classic valid anagram
    ("abcdef", "fedcba", True),     # Reversed valid anagram
    ("abcdefgh", "gfedcbaa", False) # Almost an anagram but one letter off  # noqa
])
# fmt: on
def test_isAnagram(s, t, expected):
    solution = Solution()
    assert solution.isAnagram(s, t) == expected
