from typing import List
import collections


# 994. Rotting Oranges - https://leetcode.com/problems/rotting-oranges/description/
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = collections.deque()
        fresh = 0
        rLength = len(grid)
        cLength = len(grid[0])

        for r in range(rLength):
            for c in range(cLength):
                if grid[r][c] == 2:
                    queue.append((r, c))
                if grid[r][c] == 1:
                    fresh += 1

        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        time = 0

        while fresh > 0 and queue:
            length = len(queue)

            for i in range(length):
                r, c = queue.popleft()

                for dr, dc in directions:
                    row = r + dr
                    col = c + dc

                    if (
                        row in range(rLength)
                        and col in range(cLength)
                        and grid[row][col] == 1
                    ):
                        grid[row][col] = 2
                        queue.append((row, col))
                        fresh -= 1

            time += 1

        return time if fresh == 0 else -1
