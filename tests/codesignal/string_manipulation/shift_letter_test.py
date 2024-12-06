import pytest

from src.codesignal.string_manipulation.shift_letter import solution


@pytest.mark.parametrize(
    "input_string, expected_output",
    [
        ("abc123XYz!", "bcd123YZa!"),
        ("Hello, World!", "Ifmmp, Xpsme!"),
        ("9876543210", "9876543210"),
        ("nhpq$%EPV45JZ", "oiqr$%FQW45KA"),
        ("Pythoniscool", "Qzuipojtdppm"),
        ("Zebra", "Afcsb"),
        ("InterviewPreparation", "JoufswjfxQsfqbsbujpo"),
        ("YWXyz", "ZXYza"),
        ("shift123", "tijgu123"),
        ("adZ$56Y", "beA$56Z"),
    ],
)
def test_solution(input_string, expected_output):
    assert solution(input_string) == expected_output
