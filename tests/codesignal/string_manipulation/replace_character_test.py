import pytest

from src.codesignal.string_manipulation.replace_character import solution


# fmt: off
@pytest.mark.parametrize(
    "input_string, char_to_replace, replacement_char, expected_output",
    [
        ("hello, world", "o", "a", "hella, warld"),
        ("python coding", "o", "a", "pythan cading"),
        ("replace character", "a", "o", "reploce chorocter"),
        ("practice makes perfect", "e", "i", "practici makis pirfict"),
        ("we are practicing string manipulations", "i", "o", "we are practocong strong manopulatoons"),  # noqa
        ("this function replaces one character with another", "a", "e", "this function repleces one cherecter with enother"),  # noqa
        ("keep practicing, you're doing great!", "e", "a", "kaap practicing, you'ra doing graat!"),  # noqa
        ("this is a string where each occurrence of c1 is being replaced by c2", "c", "d", "this is a string where eadh oddurrende of d1 is being repladed by d2"),  # noqa
        ("the quick brown fox jumps over the lazy dog", "o", "a", "the quick brawn fax jumps aver the lazy dag"),  # noqa
        ("all consonants are replaced by vowels", "a", "e", "ell consonents ere repleced by vowels"),  # noqa
    ],
)
# fmt: on
def test_replace_character(
    input_string, char_to_replace, replacement_char, expected_output
):
    assert (
        solution(input_string, char_to_replace, replacement_char)
        == expected_output
    )
