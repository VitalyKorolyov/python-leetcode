# 217. Contains Duplicate - https://leetcode.com/problems/contains-duplicate/description/
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        hashSet = set()

        for num in nums:
            if num in hashSet:
                return True
            hashSet.add(num)

        return False
