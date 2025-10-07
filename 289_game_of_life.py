import itertools
import pytest


def getNeighbors(board: list[list[int]], row: int, col: int) -> list[int]:
    result = []
    height = len(board)
    width = len(board[0])
    for i, j in itertools.product((-1, 0, 1), (-1, 0, 1)):
        if 0 <= row + i < height and 0 <= col + j < width:
            # corner case: same cell
            if i == 0 and j == 0:
                continue
            result.append(board[row + i][col + j])

    return result


def gameOfLife(board: list[list[int]]) -> None:
    """According to Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

    The board is made up of an m x n grid of cells, where each cell has an initial state: live (represented by a 1) or dead (represented by a 0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

        Any live cell with fewer than two live neighbors dies as if caused by under-population.
        Any live cell with two or three live neighbors lives on to the next generation.
        Any live cell with more than three live neighbors dies, as if by over-population.
        Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

    The next state of the board is determined by applying the above rules simultaneously to every cell in the current state of the m x n grid board. In this process, births and deaths occur simultaneously.

    Given the current state of the board, update the board to reflect its next state.

    Note that you do not need to return anything."""

    height = len(board)
    width = len(board[0])
    tmpBoard = [board[row][:] for row in range(height)]

    for row in range(height):
        for col in range(width):
            neighbors = getNeighbors(board, row, col)
            # Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
            liveNeighborsCount = neighbors.count(1)
            if board[row][col] == 0:
                if liveNeighborsCount == 3:
                    tmpBoard[row][col] = 1
            else:
                # Any live cell with fewer than two live neighbors dies as if caused by under-population.
                if liveNeighborsCount < 2:
                    tmpBoard[row][col] = 0

                # Any live cell with more than three live neighbors dies, as if by over-population.
                if liveNeighborsCount > 3:
                    tmpBoard[row][col] = 0

    board[:] = [tmpBoard[row][:] for row in range(height)]


@pytest.mark.parametrize(
    "board, expected",
    [
        (
            [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]],
            [[0, 0, 0], [1, 0, 1], [0, 1, 1], [0, 1, 0]],
        ),
        ([[1, 1], [1, 0]], [[1, 1], [1, 1]]),
    ],
)
def test_gameOfLife(board, expected):
    gameOfLife(board)
    assert board == expected
