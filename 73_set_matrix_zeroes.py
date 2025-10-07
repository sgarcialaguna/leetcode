import pytest


def setZeroes(matrix: list[list[int]]) -> None:
    """Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

    You must do it in place."""

    # First, collect all the rows and cols where zeroes occur
    rows: list[int] = []
    cols: list[int] = []

    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] == 0:
                rows.append(row)
                cols.append(col)

    # First, handle the rows
    for row in rows:
        for col in range(len(matrix[row])):
            matrix[row][col] = 0

    # Then, the columns
    for col in cols:
        for row in range(len(matrix)):
            matrix[row][col] = 0


@pytest.mark.parametrize(
    "matrix, expected",
    [
        ([[1, 1]], [[1, 1]]),
        ([[1, 0]], [[0, 0]]),
        ([[0], [1]], [[0], [0]]),
        ([[1, 1, 1], [1, 0, 1], [1, 1, 1]], [[1, 0, 1], [0, 0, 0], [1, 0, 1]]),
        (
            [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]],
            [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]],
        ),
    ],
)
def test_setZeroes(matrix, expected):
    setZeroes(matrix)
    assert matrix == expected
