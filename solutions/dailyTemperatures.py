# 739. Daily Temperatures - https://leetcode.com/problems/daily-temperatures/description/
class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        stack = []
        result = [0] * len(temperatures)

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][1]:
                index, _ = stack.pop()
                result[index] = i - index
            stack.append((i, t))

        return result
