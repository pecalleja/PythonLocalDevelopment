import pytest

from src.codesignal.list_operations.count_min import solution


@pytest.mark.parametrize(
    "input_list, expected_output",
    [
        ([2, 3, 4, 2, 1, 1, 5], 2),
        ([-3, -1, -1, -3, -5, -2, -3], 1),
        ([], 0),
        ([5, 5, 5, 5], 4),
        ([1], 1),
        ([-100, -100, -99, 0, 100], 2),
        ([99] * 50 + [100] * 50, 50),
        (list(range(-100, 101)), 1),
    ],
)
def test_count_min(input_list, expected_output):
    assert solution(input_list) == expected_output
