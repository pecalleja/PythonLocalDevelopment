import pytest

from src.linkedlists.lru_cache import LRUCache


def test_lru_cache():
    cache = LRUCache(2)

    # Test putting and getting values
    cache.put(1, 1)
    cache.put(2, 2)
    assert cache.get(1) == 1  # Cache is {1=1, 2=2}
    cache.put(3, 3)  # Removes key 2, cache is {1=1, 3=3}
    assert cache.get(2) == -1  # Key 2 was evicted
    cache.put(4, 4)  # Removes key 1, cache is {4=4, 3=3}
    assert cache.get(1) == -1  # Key 1 was evicted
    assert cache.get(3) == 3  # Cache is {3=3, 4=4}
    assert cache.get(4) == 4  # Cache is {3=3, 4=4}


@pytest.mark.parametrize(
    "capacity, operations, values, expected",
    [
        (
            2,
            ["put", "put", "get", "put", "get", "put", "get", "get"],
            [[1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]],
            [1, -1, -1, 3],
        ),
        (1, ["put", "put", "get"], [[1, 1], [2, 2], [1]], [-1]),
    ],
)
def test_lru_parametrize(capacity, operations, values, expected):
    cache = LRUCache(capacity)
    results = []
    for op, val in zip(operations, values):
        if op == "put":
            cache.put(val[0], val[1])
        elif op == "get":
            results.append(cache.get(val[0]))
    assert results == expected
