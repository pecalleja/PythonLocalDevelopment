import pytest

from src.codesignal.string_search.longest_common_prefix import solution


@pytest.mark.parametrize(
    "words, expected",
    [
        (["flower", "flow", "flight"], "fl"),
        (["dog", "racecar", "car"], ""),
        (["hello", "help", "helen", "helix"], "hel"),
        (["same", "same", "same"], "same"),
        (["cat", "dog", "bird"], ""),
        (["a", "a", "a"], "a"),
        (["a"], "a"),
        (["aaaa", "aaa", "aa", "a"], "a"),
        (["quick", "quack", "queue", "quest"], "qu"),
        (["train", "trainer", "training", "trains"], "train"),
    ],
)
def test_longest_common_prefix(words, expected):
    assert solution(words) == expected
