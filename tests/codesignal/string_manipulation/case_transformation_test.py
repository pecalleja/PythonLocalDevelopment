import pytest

from src.codesignal.string_manipulation.case_transformation import solution


@pytest.mark.parametrize(
    "input_string, expected_output",
    [
        ("CaSeChAnGe", "cAsEcHaNgE"),
        ("HELLO", "hello"),
        ("world", "WORLD"),
        ("f", "F"),
        ("D", "d"),
        ("S5Fg7shJ8HG789", "s5fG7SHj8hg789"),
        ("@#%AbC", "@#%aBc"),
        ("pYTHONpROGRAM", "PythonProgram"),
        ("P" * 50 + "q" * 50, "p" * 50 + "Q" * 50),
        ("", ""),
        ("abcdefghijklmnopqrstuvwxyz", "ABCDEFGHIJKLMNOPQRSTUVWXYZ"),
        ("ABCDEFGHIJKLMNOPQRSTUVWXYZ", "abcdefghijklmnopqrstuvwxyz"),
        ("aBcDeFgHiJkLmNoPqRsTuVwXyZ", "AbCdEfGhIjKlMnOpQrStUvWxYz"),
    ],
)
def test_solution(input_string, expected_output):
    assert solution(input_string) == expected_output
