import pytest

from src.neetcode.stacks.generate_parentheses import Solution


@pytest.mark.parametrize(
    "n, expected",
    [
        (1, ["()"]),
        (2, ["(())", "()()"]),
        (3, ["((()))", "(()())", "(())()", "()(())", "()()()"]),
        (
            4,
            [
                "(((())))",
                "((()()))",
                "((())())",
                "((()))()",
                "(()(()))",
                "(()()())",
                "(()())()",
                "(())(())",
                "(())()()",
                "()((()))",
                "()(()())",
                "()(())()",
                "()()(())",
                "()()()()",
            ],
        ),
        (0, [""]),
    ],
)
def test_generateParenthesis(n, expected):
    sol = Solution()
    result = sol.generateParenthesis(n)
    assert sorted(result) == sorted(expected)
