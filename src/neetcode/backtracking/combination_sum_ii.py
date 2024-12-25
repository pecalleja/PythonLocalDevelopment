class Solution:
    def combinationSum2(self, candidates, target):
        # First, sort the candidates to make it easier to handle duplicates
        candidates.sort()
        result = []
        # Start the depth-first search with initial parameters
        self._dfs(candidates, target, 0, [], result)
        return result

    def _dfs(self, candidates, target, start, path, result):
        # If the remaining target is negative, no need to proceed further
        if target < 0:
            return
        # If the target is zero, we found a valid combination
        if target == 0:
            result.append(path)
            return
        # Iterate over the candidates starting from 'start' index
        for i in range(start, len(candidates)):
            # Skip duplicates to prevent duplicate combinations
            if i > start and candidates[i] == candidates[i - 1]:
                continue
            # If the current candidate exceeds the target, break the loop
            if candidates[i] > target:
                break
            # Include the current candidate and move to the next index
            self._dfs(
                candidates,
                target - candidates[i],
                i + 1,
                path + [candidates[i]],
                result,
            )
