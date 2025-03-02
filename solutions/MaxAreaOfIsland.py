from typing import List, Set


# 695. Max Area of Island - https://leetcode.com/problems/max-area-of-island/description/
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        visited = set()

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and (i, j) not in visited:
                    maxArea = max(
                        maxArea, self.calculateIslandArea(grid, visited, i, j)
                    )

        return maxArea

    def calculateIslandArea(
        self, grid: List[List[int]], visited: Set[int], i: int, j: int
    ) -> int:
        if i < 0 or j < 0:
            return 0
        if i >= len(grid) or j >= len(grid[0]):
            return 0

        if (i, j) in visited or grid[i][j] == 0:
            return 0

        visited.add((i, j))
        area = 1

        area += self.calculateIslandArea(grid, visited, i + 1, j)
        area += self.calculateIslandArea(grid, visited, i - 1, j)
        area += self.calculateIslandArea(grid, visited, i, j + 1)
        area += self.calculateIslandArea(grid, visited, i, j - 1)

        return area
