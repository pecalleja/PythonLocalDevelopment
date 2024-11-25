from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        seen = set()
        for n in nums:
            if n in seen:
                return n
            else:
                seen.add(n)
        raise ValueError
