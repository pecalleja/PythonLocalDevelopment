import pytest

from src.codesignal.string_manipulation.vowels import solution


@pytest.mark.parametrize(
    "input_string, expected_output",
    [
        ("hello", [1, 4]),
        ("HEY", [1]),
        ("hEllOworLd", [1, 4, 6]),
        ("xyzxyz", []),
        ("aeiou", [0, 1, 2, 3, 4]),
        (
            "AEIOUAEIOUaeiouaeiou",
            [
                0,
                1,
                2,
                3,
                4,
                5,
                6,
                7,
                8,
                9,
                10,
                11,
                12,
                13,
                14,
                15,
                16,
                17,
                18,
                19,
            ],
        ),
        ("a" * 500, list(range(500))),
        ("b" * 500, []),
        ("C" * 250 + "aeiou" * 50, list(range(250, 500))),
        ("a" * 250 + "b" * 250, list(range(250))),
    ],
)
def test_solution(input_string, expected_output):
    assert solution(input_string) == expected_output
