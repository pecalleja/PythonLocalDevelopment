import pytest

from src.codesignal.recursion.all_combinations import solution


@pytest.mark.parametrize(
    "input_str,expected",
    [
        ("a", ["a"]),
        ("ab", sorted(["a", "ab", "b", "ba"])),
        (
            "abc",
            sorted(
                [
                    "a",
                    "ab",
                    "abc",
                    "ac",
                    "acb",
                    "b",
                    "ba",
                    "bac",
                    "bc",
                    "bca",
                    "c",
                    "ca",
                    "cab",
                    "cb",
                    "cba",
                ]
            ),
        ),
        ("aa", sorted(["a", "aa"])),
        ("aab", sorted(["a", "aa", "aab", "ab", "aba", "b", "ba", "baa"])),
    ],
)
def test_all_combinations(input_str, expected):
    assert sorted(solution(input_str)) == expected
