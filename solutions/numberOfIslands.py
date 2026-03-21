from typing import List


# 200. Number of Islands - https://leetcode.com/problems/number-of-islands/description/
class Solution:

    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        islands = 0
        visited = set()

        def dfs(i: int, j: int):
            if (i, j) in visited:
                return

            if i < 0 or j < 0 or i >= ROWS or j >= COLS:
                return

            if grid[i][j] == "0":
                return

            visited.add((i, j))

            for dr, dc in directions:
                dfs(i + dr, j + dc)

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == "1" and not (i, j) in visited:
                    islands += 1
                    dfs(i, j)

        return islands
