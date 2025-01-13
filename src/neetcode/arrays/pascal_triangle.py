from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        ans = [1]
        for i in range(1, rowIndex + 1):
            ans.append(ans[-1] * (rowIndex - i + 1) // i)
        return ans

    def generate(self, numRows: int) -> List[List[int]]:
        return [self.getRow(i) for i in range(numRows)]
