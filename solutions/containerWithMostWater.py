from typing import List


# 11. Container With Most Water - https://leetcode.com/problems/container-with-most-water/description/
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        maxArea = 0

        while l < r:
            area = min(height[l], height[r]) * (r - l)
            maxArea = max(area, maxArea)

            if height[l] > height[r]:
                r -= 1
            else:
                l += 1

        return maxArea
