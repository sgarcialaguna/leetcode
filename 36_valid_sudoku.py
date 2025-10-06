import pytest

LENGTH = 9


def checkRow(board: list[list[str]], row: int) -> bool:
    lookup = set()
    for number in board[row]:
        if number == ".":
            continue

        if number in lookup:
            return False

        lookup.add(number)

    return True


def checkColumn(board: list[list[str]], col: int) -> bool:
    lookup = set()
    for i in range(LENGTH):
        number = board[i][col]
        if number == ".":
            continue

        if number in lookup:
            return False

        lookup.add(number)

    return True


def checkSubboard(board: list[list[str]], index: int) -> bool:
    lookup = set()
    first_row = (index // 3) * 3
    first_col = 3 * (index % 3)

    for i in range(3):
        for j in range(3):
            number = board[first_row + i][first_col + j]
            if number == ".":
                continue

            if number in lookup:
                return False

            lookup.add(number)

    return True


def isValidSudoku(board: list[list[str]]) -> bool:
    for i in range(LENGTH):
        if not checkRow(board, i):
            return False
        if not checkColumn(board, i):
            return False
        if not checkSubboard(board, i):
            return False

    return True


@pytest.mark.parametrize(
    "board, expected",
    [
        (
            [
                ["5", "3", ".", ".", "7", ".", ".", ".", "."],
                ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                [".", "9", "8", ".", ".", ".", ".", "6", "."],
                ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                [".", "6", ".", ".", ".", ".", "2", "8", "."],
                [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                [".", ".", ".", ".", "8", ".", ".", "7", "9"],
            ],
            True,
        ),
        (
            [
                ["8", "3", ".", ".", "7", ".", ".", ".", "."],
                ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                [".", "9", "8", ".", ".", ".", ".", "6", "."],
                ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                [".", "6", ".", ".", ".", ".", "2", "8", "."],
                [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                [".", ".", ".", ".", "8", ".", ".", "7", "9"],
            ],
            False,
        ),
        (
            [
                [".", "9", ".", ".", "4", ".", ".", ".", "."],
                ["1", ".", ".", ".", ".", ".", "6", ".", "."],
                [".", ".", "3", ".", ".", ".", ".", ".", "."],
                [".", ".", ".", ".", ".", ".", ".", ".", "."],
                [".", ".", ".", "7", ".", ".", ".", ".", "."],
                ["3", ".", ".", ".", "5", ".", ".", ".", "."],
                [".", ".", "7", ".", ".", "4", ".", ".", "."],
                [".", ".", ".", ".", ".", ".", ".", ".", "."],
                [".", ".", ".", ".", "7", ".", ".", ".", "."],
            ],
            True,
        ),
    ],
)
def test_isValidSudoku(board, expected):
    assert isValidSudoku(board) is expected
