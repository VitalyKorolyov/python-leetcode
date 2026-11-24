# 73. Set Matrix Zeroes - https://leetcode.com/problems/set-matrix-zeroes/description/


class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        zeroRows, zeroColuns = set(), set()

        n, m = len(matrix), len(matrix[0])

        for i in range(0, n):
            for j in range(0, m):
                if matrix[i][j] == 0:
                    zeroRows.add(i)
                    zeroColuns.add(j)

        for i in range(0, n):
            for j in range(0, m):
                if i in zeroRows or j in zeroColuns:
                    matrix[i][j] = 0
