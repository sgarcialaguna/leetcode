import pytest


def find_next_index(height: list[int], i: int) -> int:
    max_index = -1
    for j in range(i + 1, len(height)):
        if height[j] >= height[i]:
            return j
        if height[j] >= height[max_index]:
            max_index = j

    return max_index


def trap(height: list[int]) -> int:
    trapped = 0
    i = 0

    while i < len(height):
        j = find_next_index(height, i)
        if j == -1:
            i += 1
            continue
        for k in range(i, j):
            trapped += max(0, min(height[i], height[j]) - height[k])
        i = j

    return trapped


@pytest.mark.parametrize(
    "height, expected",
    [
        ([2, 0, 2], 2),
        ([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], 6),
        ([4, 2, 0, 3, 2, 5], 9),
        ([4, 2, 3], 1),
    ],
)
def test_trap(height: list[int], expected: int):
    assert trap(height) == expected
