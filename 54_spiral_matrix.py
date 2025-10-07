import pytest

# right, down, left, up
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def spiralOrder(matrix: list[list[int]]) -> list[int]:
    """Given an m x n matrix, return all elements of the matrix in spiral order."""
    result: list[int] = []
    row, col = 0, 0
    seen: list[tuple[int, int]] = []
    width = len(matrix[0])
    height = len(matrix)
    direction = directions[0]

    while len(result) < width * height:
        # Add square to list
        seen.append((row, col))
        result.append(matrix[row][col])

        # find next square
        if (
            0 <= row + direction[0] < height
            and 0 <= col + direction[1] < width
            and (row + direction[0], col + direction[1]) not in seen
        ):
            # next coordinate is valid and not visited yer, do nothing
            pass
        else:
            # we need to switch directions
            direction = directions[(directions.index(direction) + 1) % len(directions)]

        row += direction[0]
        col += direction[1]

    return result


@pytest.mark.parametrize(
    "matrix, expected",
    [
        ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [1, 2, 3, 6, 9, 8, 7, 4, 5]),
        (
            [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]],
            [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7],
        ),
        ([[1]], [1]),
        ([[1], [2]], [1, 2]),
        ([[1, 2]], [1, 2]),
    ],
)
def test_spiralOrder(matrix, expected):
    assert spiralOrder(matrix) == expected
