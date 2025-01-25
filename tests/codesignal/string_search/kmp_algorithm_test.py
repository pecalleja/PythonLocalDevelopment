import pytest

from src.codesignal.string_search.kmp_algorithm import solution


@pytest.mark.parametrize(
    "texts, pattern, expected",
    [
        (['abcabcdabcde', 'abcdabcabcde', 'abcdfghabcdef'], 'abc', [0, 0, 0]),
        (['xyz', 'abc', 'defgh'], 'abc', [-1, 0, -1]),
        (['abcabcabc', 'abcabcabc', 'abababcabc'], 'abc', [0, 0, 4]),
        (['ggggggg', 'ghjklo', 'fghpo'], 'abc', [-1, -1, -1]),
        (['abcdefgh', 'abcdefgh'], 'abc', [0, 0]),
        ([], 'abc', []),
        (['ababc', 'ababc'], 'ab', [0, 0]),
        (['mississippi', 'ippiisspiimissi'], 'issi', [1, 11]),
        (['a' * 1000, 'a' * 1000 + 'b'], 'a' * 10, [0, 0]),
        (
            ['aaaa', 'aabb', 'xxx', 'yyy', 'zzz', 'xyy'],
            'aa',
            [0, 0, -1, -1, -1, -1],
        ),
        (['a' * 100 + 'b' + 'a' * 100], 'b', [100]),
        (['', '', ''], 'pat', [-1, -1, -1]),
        (
            ['patterninmiddle', 'midpattern', 'patternend'],
            'pattern',
            [0, 3, 0],
        ),
        (['abababab', 'bababa', 'ababab'], 'abab', [0, 1, 0]),
        (['abcdefghij', 'ghijabcdef', 'defghij'], 'defg', [3, -1, 0]),
        (
            ['abccbaabccba', 'aaabbbaaa', 'bbbaaa', 'cccbbb', 'aaaa'],
            'aaa',
            [-1, 0, 3, -1, 0],
        ),
        (
            ['abcabcabcabc', 'abcabcabcabc', 'abcabcabcabc'],
            'abcabc',
            [0, 0, 0],
        ),
        (['qwertyuiop', 'zxcvbnmasd', 'lkjhgfdsqwert'], 'wert', [1, -1, 9]),
        (['testtesting', 'testingtest', 'test'], 'test', [0, 0, 0]),
        (['nomatch', 'anotherone', 'thisonetoo'], 'nomatchhere', [-1, -1, -1]),
    ],
)
def test_find_pattern_in_texts(texts, pattern, expected):
    assert solution(texts, pattern) == expected
