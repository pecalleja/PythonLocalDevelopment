import pytest

from src.codesignal.bit_manipulation.unset_bit import solution


@pytest.mark.parametrize(
    "input_value, expected_output",
    [
        (9, 30),
        (1, 31),
        (16, 31),
        (0, 32),
        (15, 28),
        (32, 31),
        (31, 27),
        (1024, 31),
        (1000000, 25),
        (2147483648, 31),
        (1073741823, 2),
        (1073741824, 31),
        (536870911, 3),
        (536870912, 31),
    ],
)
def test_count_unset_bits(input_value, expected_output):
    assert solution(input_value) == expected_output
