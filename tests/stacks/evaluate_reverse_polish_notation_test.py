import pytest

from src.stacks.evaluate_reverse_polish_notation import Solution


# fmt: off
@pytest.mark.parametrize(
    "tokens, expected",
    [
        (["2", "1", "+", "3", "*"], 9),
        (["4", "13", "5", "/", "+"], 6),
        (["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"], 22),  # noqa
        (["3", "11", "+", "5", "-"], 9),
        (["18"], 18),
        (["10", "2", "/", "3", "*"], 15),
        (["5", "1", "2", "+", "4", "*", "+", "3", "-"], 14),
        (["0", "3", "/"], 0),
        (["2", "3", "*"], 6),
    ],
)
# fmt: on
def test_evalRPN(tokens, expected):
    sol = Solution()
    assert sol.evalRPN(tokens) == expected
