from typing import List

import pytest


def canJumpPastIndex(nums: List[int], i: int):
    for j in range(i - 1, -1, -1):
        if j + nums[j] > i or j + nums[j] >= len(nums) - 1:
            return True

    return False


def canJump(nums: List[int]):
    if 0 not in nums:
        return True

    if nums == [0]:
        return True

    for i in range(len(nums) - 1, -1, -1):
        if nums[i] > 0:
            continue

        if not canJumpPastIndex(nums, i):
            return False

    return True


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
