from typing import List

# 59. Spiral Matrix II - https://leetcode.com/problems/spiral-matrix-ii/description/
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        count = 1

        l, r, t, b = 0, n - 1, 0, n - 1
        result = [[0] * n for _ in range(n)]

        while l <= r and t <= b:
            for row in range(l, r + 1):
                result[t][row] = count
                count += 1
            t += 1

            for col in range(t, b + 1):
                result[col][r] = count
                count += 1
            r -= 1

            if t <= b:
                for row in range(r, l - 1, -1):
                    result[b][row] = count
                    count += 1
                b -= 1

            if l <= r:
                for col in range(b, t - 1, -1):
                    result[col][l] = count
                    count += 1
                l += 1

        return result