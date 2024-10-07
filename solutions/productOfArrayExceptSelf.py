from typing import List

# 238. Product of Array Except Self - https://leetcode.com/problems/product-of-array-except-self/submissions/1415245316/
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left = [1] * n
        right = [1] * n

        for i in range(1, n):
            left[i] = nums[i - 1] * left[i - 1]

        for i in range(n - 2, -1, -1):
            right[i] = nums[i + 1] * right[i + 1]

        result = [0] * n
        for i in range(n):
            result[i] = left[i] * right[i]

        return result
