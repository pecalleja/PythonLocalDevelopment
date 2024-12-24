from typing import List


class Solution:
    def combinationSum(
        self, candidates: List[int], target: int
    ) -> List[List[int]]:
        def backtrack(start, target, path):
            if target == 0:
                result.append(list(path))
                return
            if target < 0:
                return

            for i in range(start, len(candidates)):
                # Include candidates[i] in the combination and reduce target
                path.append(candidates[i])
                backtrack(
                    i, target - candidates[i], path
                )  # 'i' allows reuse of the same number
                path.pop()  # Backtrack

        result = []
        backtrack(0, target, [])
        return result
