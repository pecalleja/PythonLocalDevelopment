import pytest

from src.slidingwindow.longest_repeating_character_replacement import Solution


@pytest.mark.parametrize(
    "s, k, expected",
    [
        ("ABAB", 2, 4),
        ("AABABBA", 1, 4),
        ("AAAA", 2, 4),
        ("ABCD", 2, 3),
        ("A", 0, 1),
        ("ABAA", 0, 2),
        ("ABAB", 1, 3),
        ("ABAAAB", 2, 6),
    ],
)
def test_characterReplacement(s, k, expected):
    solution = Solution()
    assert solution.characterReplacement(s, k) == expected
