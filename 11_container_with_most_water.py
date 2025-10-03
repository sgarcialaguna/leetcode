import pytest


def area(height: list[int], start: int, end: int) -> int:
    return min(height[start], height[end]) * (end - start)


def maxArea(height: list[int]):
    result = 0
    left = 0
    right = len(height) - 1
    while left < right:
        result = max(area(height, left, right), result)
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return result


@pytest.mark.parametrize(
    "height, expected", [([1, 1], 1), ([1, 8, 6, 2, 5, 4, 8, 3, 7], 49)]
)
def test_maxArea(height, expected):
    assert maxArea(height) == expected
