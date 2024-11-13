import bisect
from collections import defaultdict


class TimeMap:
    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""

        timestamps = self.store[key]
        i = bisect.bisect_right(timestamps, (timestamp, chr(127)))

        return timestamps[i - 1][1] if i else ""
