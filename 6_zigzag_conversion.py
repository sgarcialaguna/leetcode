import pytest


def convertToMatrix(s: str, numRows: int) -> list[list[str]]:
    cols = []
    j = 0
    k = numRows - 2

    col = 0
    for c in s:
        if len(cols) <= col:
            cols.append([""] * numRows)

        if col % (numRows - 1) == 0:
            # This column will be filled with characters
            cols[col][j] = c
            if cols[col][numRows - 1]:
                col += 1
            j += 1
            j = j % numRows
        else:
            # This column will have exactly one character
            cols[col][k] = c
            k -= 1
            if k == 0:
                k = numRows - 2
            col += 1

    return cols


def convert(s: str, numRows: int) -> str:
    if numRows == 1:
        return s

    matrix = convertToMatrix(s, numRows)
    result = ""
    for j in range(numRows):
        for i in range(len(matrix)):
            c = matrix[i][j]
            if c:
                result += c

    return result


@pytest.mark.parametrize(
    "s, numRows, expected",
    [
        (
            "PAYPALISHIRING",
            3,
            [
                ["P", "A", "Y"],
                ["", "P", ""],
                ["A", "L", "I"],
                ["", "S", ""],
                ["H", "I", "R"],
                ["", "I", ""],
                ["N", "G", ""],
            ],
        ),
        (
            "PAYPALISHIRING",
            4,
            [
                ["P", "A", "Y", "P"],
                ["", "", "A", ""],
                ["", "L", "", ""],
                ["I", "S", "H", "I"],
                ["", "", "R", ""],
                ["", "I", "", ""],
                ["N", "G", "", ""],
            ],
        ),
    ],
)
def test_convertToMatrix(s, numRows, expected):
    assert convertToMatrix(s, numRows) == expected


@pytest.mark.parametrize(
    "s, numRows, expected",
    [
        ("PAYPALISHIRING", 3, "PAHNAPLSIIGYIR"),
        ("PAYPALISHIRING", 4, "PINALSIGYAHRPI"),
        ("A", 1, "A"),
    ],
)
def test_convert(s, numRows, expected):
    assert convert(s, numRows) == expected
