from collections import defaultdict
from typing import List

import pytest


def canJump(nums: List[int]):
    # See https://www.youtube.com/watch?v=CsDI-yQuGeM
    smallest = 0
    n = len(nums)
    end, far = 0, 0

    for i in range(n - 1):
        far = max(far, i + nums[i])
        if i == end:
            smallest += 1
            end = far

    return smallest


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([2, 3, 1, 1, 4], 2),
        ([2, 3, 0, 1, 4], 2),
    ],
)
def test_canJump(nums: List[int], expected: bool):
    assert canJump(nums) == expected
