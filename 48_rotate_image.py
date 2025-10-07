import pytest


def rotate(matrix: list[list[int]]) -> None:
    """You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

    You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation."""

    # First, transpose the matrix
    # Clever solution for transposing, but not allowed due to the constraints
    # matrix[:] = [list(i) for i in zip(*matrix)]
    for i in range(len(matrix)):
        for j in range(i, len(matrix)):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Then, reverse each row
    for row in matrix:
        row.reverse()
    return


@pytest.mark.parametrize(
    "matrix, expected",
    [
        ([[1]], [[1]]),
        ([[1, 2], [3, 4]], [[3, 1], [4, 2]]),
        ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[7, 4, 1], [8, 5, 2], [9, 6, 3]]),
        (
            [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]],
            [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]],
        ),
    ],
)
def test_rotate(matrix, expected):
    rotate(matrix)
    assert matrix == expected
