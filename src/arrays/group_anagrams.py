from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = {}
        for s in strs:
            sorted_str = "".join(sorted(s))
            if sorted_str in ans:
                ans[sorted_str].append(s)
            else:
                ans[sorted_str] = [s]
        return list(ans.values())
