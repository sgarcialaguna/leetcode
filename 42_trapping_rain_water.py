import pytest


def find_next_index(height: list[int], i: int) -> int:
    max_index = -1
    for j in range(i + 1, len(height)):
        if height[j] >= height[i]:
            return j
        if height[j] >= height[max_index]:
            max_index = j

    return max_index


def is_strictly_increasing(l: list[int]):
    return all(x < y for x, y in zip(l, l[1:]))


def is_strictly_decreasing(l: list[int]):
    return all(x > y for x, y in zip(l, l[1:]))


def trap(height: list[int]) -> int:
    if is_strictly_decreasing(height) or is_strictly_increasing(height):
        return 0

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
        (range(20000, 0, -1), 0),
    ],
)
def test_trap(height: list[int], expected: int):
    assert trap(height) == expected
