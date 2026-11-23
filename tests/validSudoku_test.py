import pytest

from solutions.validSudoku import Solution

VALID_BOARD = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
]


def board_with_entries(*entries):
    board = [["."] * 9 for _ in range(9)]
    for row, column, value in entries:
        board[row][column] = value
    return board


def test_accepts_a_valid_partial_board():
    assert Solution().isValidSudoku(VALID_BOARD) is True


def test_accepts_an_empty_board():
    assert Solution().isValidSudoku([["."] * 9 for _ in range(9)]) is True


@pytest.mark.parametrize(
    "board",
    [
        # Duplicate in a row, but in different columns and 3x3 boxes.
        board_with_entries((0, 0, "1"), (0, 4, "1")),
        # Duplicate in a column, but in different rows and 3x3 boxes.
        board_with_entries((0, 0, "1"), (4, 0, "1")),
        # Duplicate in a 3x3 box, but in different rows and columns.
        board_with_entries((0, 0, "1"), (1, 1, "1")),
    ],
    ids=["duplicate-row", "duplicate-column", "duplicate-box"],
)
def test_rejects_duplicates_in_any_sudoku_constraint(board):
    assert Solution().isValidSudoku(board) is False
