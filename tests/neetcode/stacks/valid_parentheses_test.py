import pytest

from src.neetcode.stacks.valid_parentheses import Solution


@pytest.mark.parametrize(
    "s, expected",
    [
        ("()", True),  # Simple valid parentheses
        ("()[]{}", True),  # Multiple types of parentheses, valid
        ("(]", False),  # Different types of parentheses, invalid
        ("([)]", False),  # Wrong order, invalid
        ("{[]}", True),  # Nested valid parentheses
        ("", True),  # Empty string, valid
        ("(", False),  # Single open parenthesis, invalid
        (")", False),  # Single close parenthesis, invalid
        ("((()))", True),  # Multiple nested parentheses
        ("[{()}]", True),  # Complex valid case with mixed types
        ("[{(})]", False),  # Complex invalid case
    ],
)
def test_isValid(s, expected):
    solution = Solution()

    # Test the isValid function
    result = solution.isValid(s)

    # Assert the result is as expected
    assert result == expected
