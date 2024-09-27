from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        ans = [1]
        for i in range(1, rowIndex + 1):
            last_element = ans[-1]
            position = rowIndex - i + 1
            value = last_element * position
            ans.append(value // i)
        return ans
