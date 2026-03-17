from typing import List


# 14. Longest Common Prefix - https://leetcode.com/problems/longest-common-prefix/description/
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""

        first = strs[0]

        for i in range(len(first)):
            for j in range(1, len(strs)):
                if len(strs[j]) <= i:
                    return first[:i]

                if first[i] != strs[j][i]:
                    return i == 0 if "" else first[:i]

        return first
