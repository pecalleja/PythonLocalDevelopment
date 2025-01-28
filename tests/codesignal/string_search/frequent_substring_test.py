import pytest

from src.codesignal.string_search.frequent_substring import solution

# Test cases structured as (input_text, length, expected_result)
test_cases = [
    ('abrakadabraka', 3, 2),
    ('mississippi', 2, 2),
    ('aaa', 1, 3),
    ('a', 1, 1),
    ('abcdefg', 3, 1),
    ('banana', 1, 3),
    ('abcabcabc', 3, 3),
    ('abcabcabc', 2, 3),
    ('abcdefghijklmnopqrstuvwxyz', 5, 1),
    ('abcdefghijklmnopqrstuvwxyz', 1, 1),
    ('abcdefghijklmnopqrstuvwxyz' * 5, 26, 5),
    ('abcdefghijklmnopqrstuvwxyz' * 5, 10, 5),
    ('repetitionsrepetitions', 10, 2),
    ('abcabcabcabcabc', 1, 5),
    ('abcabcabcabcabc', 2, 5),
    ('abcabcabcabcabc', 5, 4),
]


@pytest.mark.parametrize("input_text, length, expected", test_cases)
def test_max_substring_occurrences(input_text, length, expected):
    assert solution(input_text, length) == expected


# Additional edge cases that might be worth testing
edge_cases = [
    ('', 1, 0),  # Empty string
    ('abc', 4, 0),  # Length longer than string
    ('🌟🌟🌟', 1, 3),  # Unicode characters
    ('  ', 1, 2),  # Whitespace
]


@pytest.mark.parametrize("input_text, length, expected", edge_cases)
def test_max_substring_occurrences_edge_cases(input_text, length, expected):
    assert solution(input_text, length) == expected


# Test for invalid inputs
def test_invalid_inputs():
    with pytest.raises(TypeError):
        solution(123, 1)
