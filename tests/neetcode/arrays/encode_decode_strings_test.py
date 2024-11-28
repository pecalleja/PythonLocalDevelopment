import pytest

from src.neetcode.arrays.encode_decode_strings import Codec


@pytest.mark.parametrize(
    "strs",
    [
        (["hello", "world"]),  # Simple case with two words
        ([""]),  # Empty string in the list
        (["a", ""]),  # Mixed empty and non-empty strings
        (["abc", "def", "ghi"]),  # Simple case with multiple strings
        (["123", "456", "789"]),  # Strings with numbers
        (["!@#", "$%^", "&*()"]),  # Strings with special characters
        (["a" * 1000, "b" * 2000]),  # Long strings
        (["", "", "", ""]),  # All empty strings
        (["foo", "bar", "baz", "", "qux"]),  # Mixed strings with empty string
    ],
)
def test_encode_decode(strs):
    codec = Codec()
    encoded = codec.encode(strs)
    assert isinstance(encoded, str)
    decoded = codec.decode(encoded)
    assert isinstance(decoded, list)
    assert decoded == strs
