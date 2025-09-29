import pytest


def trap(height: list[int]) -> int:
    trapped = 0
    i = 0

    maxLeft = [0] * len(height)
    for i in range(1, len(height)):
        maxLeft[i] = max(maxLeft[i - 1], height[i - 1])

    maxRight = [0] * len(height)
    for i in range(len(height) - 2, -1, -1):
        maxRight[i] = max(maxRight[i + 1], height[i + 1])

    minLeftRight = [min(maxLeft[i], maxRight[i]) for i in range(len(height))]

    for i in range(len(height)):
        trapped += max(0, minLeftRight[i] - height[i])

    return trapped


@pytest.mark.parametrize(
    "height, expected",
    [
        ([2, 0, 2], 2),
        ([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], 6),
        ([4, 2, 0, 3, 2, 5], 9),
        ([4, 2, 3], 1),
        (range(20000, 0, -1), 0),
    ],
)
def test_trap(height: list[int], expected: int):
    assert trap(height) == expected
