from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        total = len(nums)
        for i in range(total - 1):
            for j in range(i + 1, total):
                if nums[i] + nums[j] == target:
                    return [i, j]
