from collections import defaultdict
from typing import List

# 49. Group Anagrams - https://leetcode.com/problems/group-anagrams/description/
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = defaultdict(list)

        for s in strs:
            count = [0] * 26

            for c in s:
                count[ord(c) - ord("a")] += 1

            hashMap[tuple(count)].append(s)

        return list(hashMap.values())