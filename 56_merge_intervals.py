import pytest


def merge(intervals: list[list[int]]) -> list[list[int]]:
    """Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals,
    and return an array of the non-overlapping intervals that cover all the intervals in the input."""

    if not intervals or not intervals[0]:
        return [[]]

    starts, ends = zip(*intervals)
    starts, ends = sorted(starts), sorted(ends)

    result: list[list[int]] = [[starts[0], ends[0]]]
    for i in range(len(intervals) - 1):
        lastInterval = result[len(result) - 1]
        if starts[i + 1] <= ends[i]:
            lastInterval[1] = ends[i + 1]
        else:
            result.append([starts[i + 1], ends[i + 1]])

    return result


@pytest.mark.parametrize(
    "intervals, expected",
    [
        ([[]], [[]]),
        ([[1, 2]], [[1, 2]]),
        ([[1, 2], [2, 3]], [[1, 3]]),
        ([[2, 3], [1, 2]], [[1, 3]]),
        ([[1, 3], [2, 6], [8, 10], [15, 18]], [[1, 6], [8, 10], [15, 18]]),
        ([[1, 4], [4, 5]], ([[1, 5]])),
        ([[4, 7], [1, 4]], [[1, 7]]),
    ],
)
def test_merge(intervals, expected):
    assert merge(intervals) == expected
