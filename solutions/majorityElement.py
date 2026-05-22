from typing import List


# 169. Majority Element - https://leetcode.com/problems/majority-element/description/
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res, count = nums[0], 1

        for i in range(1, len(nums)):
            if count == 0:
                res = nums[i]
            count += 1 if res == nums[i] else -1

        return res

    def majorityElementHashMap(self, nums: List[int]) -> int:
        count = {}

        res, maxCount = 0, 0

        for n in nums:
            count[n] = 1 + count.get(n, 0)
            res = n if count[n] > maxCount else res
            maxCount = max(count[n], maxCount)

        return res
