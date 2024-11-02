from typing import List


# 853. Car Fleet - https://leetcode.com/problems/car-fleet/description/
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = []

        for p, s in zip(position, speed):
            pairs.append((p, s))

        pairs.sort(reverse=True)
        stack = []

        for p, s in pairs:
            stack.append((target - p) / s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)
