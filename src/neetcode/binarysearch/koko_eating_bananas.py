import math
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)

        while left < right:
            mid = (left + right) // 2
            hours_needed = sum(math.ceil(pile / mid) for pile in piles)

            if hours_needed <= h:
                right = mid
            else:
                left = mid + 1

        return left
