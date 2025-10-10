from functools import cmp_to_key
from operator import itemgetter
import pytest


def compareTwoPoints(left, right):
    if left[0] == right[0]:
        return left[1] - right[1]

    return left[0] - right[0]


def findMinArrowShots(points: list[list[int]]) -> int:
    """There are some spherical balloons taped onto a flat wall that represents the XY-plane.
    The balloons are represented as a 2D integer array points where points[i] = [xstart, xend] denotes
    a balloon whose horizontal diameter stretches between xstart and xend.
    You do not know the exact y-coordinates of the balloons.

    Arrows can be shot up directly vertically (in the positive y-direction) from different points
    along the x-axis. A balloon with xstart and xend is burst by an arrow shot at x if xstart <= x <= xend.
    There is no limit to the number of arrows that can be shot. A shot arrow keeps traveling up infinitely,
    bursting any balloons in its path.

    Given the array points, return the minimum number of arrows that must be shot to burst all balloons."""

    # Basic idea: Start with result equal to the number of balloons. Sort the list of points by starting points
    # Find how many ranges overlap. For each overlap, subtract one

    points.sort()
    result = len(points)
    left, right = 0, 1
    currentRange = points[left]
    while right < len(points):
        # Find the minimum overlap covering all points so far
        overlap = [
            max(currentRange[0], points[right][0]),
            min(currentRange[1], points[right][1]),
        ]
        # While endpoint >= startpoint, we still have an overlap
        if overlap[1] - overlap[0] >= 0:
            right += 1
            result -= 1
            currentRange = overlap
        else:
            left = right
            right = left + 1
            currentRange = points[left]

    return result


@pytest.mark.parametrize(
    "points, expected",
    [
        ([[1, 1], [1, 1]], 1),
        ([[1, 1], [2, 2]], 2),
        ([[10, 16], [2, 8], [1, 6], [7, 12]], 2),
        ([[1, 2], [3, 4], [5, 6], [7, 8]], 4),
        ([[1, 2], [2, 3], [3, 4], [4, 5]], 2),
        (
            [
                [3, 9],
                [7, 12],
                [3, 8],
                [6, 8],
                [9, 10],
                [2, 9],
                [0, 9],
                [3, 9],
                [0, 6],
                [2, 8],
            ],
            2,
        ),
        ([[9, 12], [1, 10], [4, 11], [8, 12], [3, 9], [6, 9], [6, 7]], 2),
    ],
)
def test_findMinArrowShots(points, expected):
    assert findMinArrowShots(points) == expected
