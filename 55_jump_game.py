from typing import List

import pytest


def canJump(nums: List[int]):
    n = len(nums)
    goal = n - 1
    for i in range(n - 1, -1, -1):
        if i + nums[i] >= goal:
            goal = i

    return goal == 0


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([2, 3, 1, 1, 4], True),
        ([3, 2, 1, 0, 4], False),
        ([0], True),
        ([2, 0], True),
        ([1, 1, 2, 2, 0, 1, 1], True),
        ([2, 0, 0], True),
    ],
)
def test_canJump(nums: List[int], expected: bool):
    assert canJump(nums) == expected
