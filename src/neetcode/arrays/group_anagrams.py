from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_groups = defaultdict(list)
        for s in strs:
            sorted_key = tuple(sorted(s))
            anagram_groups[sorted_key].append(s)

        result = []
        for group in anagram_groups.values():
            result.append(sorted(group))

        result.sort(key=lambda x: x[0])

        return result
