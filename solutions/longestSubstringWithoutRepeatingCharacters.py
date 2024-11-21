# 3. Longest Substring Without Repeating Characters - https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hash = set()
        maxLength = 0
        l = 0

        for r in range(len(s)):
            while s[r] in hash:
                hash.remove(s[l])
                l += 1

            hash.add(s[r])
            maxLength = max(maxLength, r - l + 1)

        return maxLength
