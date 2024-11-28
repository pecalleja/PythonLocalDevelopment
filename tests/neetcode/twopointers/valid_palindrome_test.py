import pytest

from src.neetcode.twopointers.valid_palindrome import Solution


@pytest.mark.parametrize(
    "s, expected",
    [
        ("A man, a plan, a canal: Panama", True),
        ("race a car", False),
        ("", True),
        (" ", True),
        ("0P", False),
        ("No lemon, no melon", True),
        ("12321", True),
        ("123456", False),
        ("Was it a car or a cat I saw?", True),
        ("Able was I, I saw elba", True),
    ],
)
def test_isPalindrome(s, expected):
    sol = Solution()
    assert sol.isPalindrome(s) == expected
