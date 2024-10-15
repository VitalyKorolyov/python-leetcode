from typing import List


# 167. Two Sum II - Input Array Is Sorted - https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1

        while l < r:
            current = numbers[l] + numbers[r]

            if current == target:
                return [l + 1, r + 1]
            if current > target:
                r -= 1
            if current < target:
                l += 1

        return []
