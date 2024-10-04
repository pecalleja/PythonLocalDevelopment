import pytest

from src.recursion.k_symbol import Solution


@pytest.mark.parametrize(
    "n, k, expected",
    [
        (1, 1, 0),  # Base case, first row
        (2, 1, 0),  # Row 2, first symbol (same as row 1)
        (2, 2, 1),  # Row 2, second symbol (complement of row 1)
        (3, 1, 0),  # Row 3, first symbol (same as row 2)
        (3, 3, 1),  # Row 3, third symbol (complement of row 2)
        (4, 5, 1),  # Row 4, fifth symbol
        (4, 8, 1),  # Row 4, last symbol
        (30, 434991989, 0),  # Large input case
    ],
)
def test_kthGrammar(n, k, expected):
    solution = Solution()
    result = solution.kthGrammar(n, k)
    assert result == expected
