from typing import List


#1929. Concatenation of Array - https://leetcode.com/problems/concatenation-of-array/description/
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        length = len(nums)
        ans = [0] * length * 2

        for i in range(length):
            ans[i] = nums[i]
            ans[i + length] = nums[i]

        return ans
