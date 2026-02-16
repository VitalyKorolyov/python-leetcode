# 28. Find the Index of the First Occurrence in a String - https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        nL = len(needle)
        hayL = len(haystack)

        if hayL < nL:
            return -1

        for i in range(hayL):
            if haystack[i: i+nL] == needle:
                return i

        return -1
