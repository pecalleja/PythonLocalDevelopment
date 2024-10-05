from collections import Counter
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        elements = Counter(nums)
        return [x[0] for x in elements.most_common(k)]
