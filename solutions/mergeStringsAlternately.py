# 1768. Merge Strings Alternately - https://leetcode.com/problems/merge-strings-alternately/description/
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        minLength = len(word2) if len(word1) > len(word2) else len(word1)
        result = ""

        for i in range(minLength):
            result += word1[i] + word2[i]

        result += word1[minLength:]
        result += word2[minLength:]

        return "".join(result)
