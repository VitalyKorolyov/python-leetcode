import pytest

from solutions.setMatrixZeroes import Solution


@pytest.mark.parametrize(
    ("matrix", "expected"),
    [
        (
            [[1, 1, 1], [1, 0, 1], [1, 1, 1]],
            [[1, 0, 1], [0, 0, 0], [1, 0, 1]],
        ),
        (
            [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]],
            [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]],
        ),
        (
            [[1, 2], [3, 4]],
            [[1, 2], [3, 4]],
        ),
        (
            [[1, 0, 3]],
            [[0, 0, 0]],
        ),
        (
            [[1], [0], [3]],
            [[0], [0], [0]],
        ),
    ],
    ids=[
        "middle-zero",
        "zeros-in-first-row",
        "no-zeros",
        "single-row",
        "single-column",
    ],
)
def test_set_zeroes_updates_matrix_in_place(matrix, expected):
    result = Solution().setZeroes(matrix)

    assert result is None
    assert matrix == expected
