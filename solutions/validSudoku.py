from typing import List


# 36. Valid Sudoku - https://leetcode.com/problems/valid-sudoku/description/
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = [set() for _ in range(9)]
        rows = [set() for _ in range(9)]
        squares = [[set() for _ in range(3)] for _ in range(3)]

        for r in range(9):
            for c in range(9):
                cellValue = board[r][c]
                if cellValue == ".":
                    continue

                if cellValue in rows[r]:
                    return False
                if cellValue in cols[c]:
                    return False
                if cellValue in squares[r // 3][c // 3]:
                    return False

                rows[r].add(cellValue)
                cols[c].add(cellValue)
                squares[r // 3][c // 3].add(cellValue)

        return True
