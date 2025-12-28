from typing import List


# 26. Remove Duplicates from Sorted Array - https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)

        insertIndex: int = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[insertIndex] = nums[i]
                insertIndex += 1

        return insertIndex
