import pytest

from src.codesignal.bit_manipulation.lone_bit import solution


@pytest.mark.parametrize(
    "input_value, expected_output",
    [
        (16, 5),
        (13, -1),
        (0, -1),
        (8, 4),
        (2, 2),
        (1, 1),
        (64, 7),
        (1024, 11),
        (15, -1),
        (512, 10),
    ],
)
def test_find_lone_set_bit(input_value, expected_output):
    assert solution(input_value) == expected_output
