import pytest

# Guess having modules with numbers was a dumb idea. Oh well.
merge = __import__("56_merge_intervals").merge


def insert(intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
    """You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent
    the start and the end of the ith interval and intervals is sorted in ascending order by starti.
    You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

    Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and
    intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

    Return intervals after the insertion.

    Note that you don't need to modify intervals in-place. You can make a new array and return it."""

    # Really just a special case of merging
    return merge([*intervals, newInterval])


@pytest.mark.parametrize(
    "intervals,newInterval, expected",
    [
        ([[]], [], [[]]),
        ([[1, 2]], [2, 3], [[1, 3]]),
        ([[1, 3], [6, 9]], [2, 5], [[1, 5], [6, 9]]),
        (
            [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]],
            [4, 8],
            [[1, 2], [3, 10], [12, 16]],
        ),
    ],
)
def test_merge(intervals, newInterval, expected):
    assert insert(intervals, newInterval) == expected
