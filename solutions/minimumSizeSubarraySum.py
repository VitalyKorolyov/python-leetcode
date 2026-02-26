from typing import List


# 209. Minimum Size Subarray Sum - https://leetcode.com/problems/minimum-size-subarray-sum/description/
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        length = len(nums)
        answer = float("inf")
        sum = 0
        l = 0

        for r in range(length):
            sum += nums[r]
            while sum >= target:
                answer = min(r - l + 1, answer)
                sum -= nums[l]
                l += 1

        return 0 if answer == float("inf") else answer
