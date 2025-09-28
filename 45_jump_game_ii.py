from collections import defaultdict
from typing import List

import pytest


def canJump(nums: List[int]):
    reachable_positions = {}
    for i, num in enumerate(nums):
        for j in range(i + 1, min(i + num + 1, len(nums))):
            if j in reachable_positions:
                continue
            reachable_positions[j] = i

    i = len(nums) - 1
    jumps = 0
    while i > 0:
        jumps += 1
        i = reachable_positions[i]

    return jumps


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([2, 3, 1, 1, 4], 2),
        ([2, 3, 0, 1, 4], 2),
    ],
)
def test_canJump(nums: List[int], expected: bool):
    assert canJump(nums) == expected
