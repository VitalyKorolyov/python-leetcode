# 62. Unique Paths - https://leetcode.com/problems/unique-paths/description/
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}
        return self.dfs(0, 0, memo, m, n)

    def dfs(self, x: int, y: int, memo: dict, m: int, n: int) -> int:
        if x == m - 1 and y == n - 1:
            return 1
        if x >= m or y >= n:
            return 0
        if (x, y) in memo:
            return memo[(x, y)]
        memo[(x, y)] = self.dfs(x + 1, y, memo, m, n) + self.dfs(x, y + 1, memo, m, n)
        return memo[(x, y)]
