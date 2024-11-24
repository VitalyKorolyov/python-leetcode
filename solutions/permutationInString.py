# 567. Permutation in String - https://leetcode.com/problems/permutation-in-string/description/
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        count1 = {}
        for c in s1:
            count1[c] = 1 + count1.get(c, 0)

        count2 = {}
        l = 0
        for r in range(len(s2)):
            cToAdd = s2[r]
            count2[cToAdd] = 1 + count2.get(cToAdd, 0)

            if r < len(s1) - 1:
                continue

            if count1 == count2:
                return True

            cToRemove = s2[l]
            count2[cToRemove] -= 1
            if count2[cToRemove] == 0:
                del count2[cToRemove]

            l += 1

        return False
