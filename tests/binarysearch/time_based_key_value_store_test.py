from src.binarysearch.time_based_key_value_store import TimeMap


def test_time_based_key_value_store():
    time_map = TimeMap()

    # Setting values at various timestamps
    time_map.set("foo", "bar", 1)
    time_map.set("foo", "bar2", 4)

    # Test retrieving exact timestamps
    assert time_map.get("foo", 1) == "bar"
    assert time_map.get("foo", 4) == "bar2"

    # Test retrieving a timestamp without a direct match
    assert time_map.get("foo", 3) == "bar"  # Closest previous timestamp is 1
    assert time_map.get("foo", 5) == "bar2"  # Closest previous timestamp is 4

    # Test when the key has no entries at all
    assert time_map.get("bar", 1) == ""

    # Test retrieving timestamp earlier than any set timestamp
    assert time_map.get("foo", 0) == ""

    # Multiple sets and gets
    time_map.set("foo", "bar3", 10)
    assert time_map.get("foo", 10) == "bar3"
    assert time_map.get("foo", 6) == "bar2"  # Closest timestamp before 6 is 4
    assert (
        time_map.get("foo", 11) == "bar3"
    )  # Closest timestamp before 11 is 10
