from typing import List


class Solution:
    def dailyTemperatures(self, t: List[int]) -> List[int]:
        length = len(t)
        ans = [0] * length
        stack = []
        for curr, temp in enumerate(t):
            while stack and t[stack[-1]] < temp:
                prev = stack.pop()
                ans[prev] = curr - prev
            stack.append(curr)
        return ans
