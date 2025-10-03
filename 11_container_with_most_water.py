import itertools
import pytest


def area(height: list[int], start: int, end: int) -> int:
    return min(height[start], height[end]) * (end - start)


def maxArea(height: list[int]):
    result = 0
    for start, end in itertools.combinations(range(len(height)), 2):
        result = max(result, area(height, start, end))

    return result


@pytest.mark.parametrize(
    "height, expected", [([1, 1], 1), ([1, 8, 6, 2, 5, 4, 8, 3, 7], 49)]
)
def test_maxArea(height, expected):
    assert maxArea(height) == expected
