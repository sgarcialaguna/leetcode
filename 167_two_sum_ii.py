from logging import raiseExceptions
from typing import Optional
import pytest


def binary_search(
    haystack: list[int], needle: int, lo: Optional[int] = None, hi: Optional[int] = None
):
    lo = lo or 0
    hi = hi or len(haystack) - 1

    while lo <= hi:
        mid = (lo + hi) // 2
        val = haystack[mid]

        if val == needle:
            return mid

        if val < needle:
            lo = mid + 1
        else:
            hi = mid - 1

    return -1


def twoSum_binarysearch(nums: list[int], target: int) -> list[int]:
    for idx, num in enumerate(nums):
        lo = None
        target2 = target - num
        if target2 >= num:
            lo = idx + 1
        else:
            # We've already had this combination
            continue
        idx2 = binary_search(nums, target2, lo)
        if idx2 != -1:
            return [idx + 1, idx2 + 1]
    raise Exception("OH NOES")


def twoSum_twoPointers(nums: list[int], target: int) -> list[int]:
    lo = 0
    hi = len(nums) - 1

    while lo < hi:
        if nums[lo] + nums[hi] > target:
            hi -= 1
        elif nums[lo] + nums[hi] < target:
            lo += 1
        else:
            return [lo + 1, hi + 1]

    raise Exception("OH NOES")


@pytest.mark.parametrize(
    "nums, target, expected",
    [
        ([2, 7, 11, 15], 9, [1, 2]),
        ([2, 3, 4], 6, [1, 3]),
        ([-1, 0], -1, [1, 2]),
        ([1, 2, 3, 4, 4, 9, 56, 90], 8, [4, 5]),
    ],
)
def test_twoSum(nums: list[int], target: int, expected: list[int]):
    # assert twoSum_binarysearch(nums, target) == expected
    assert twoSum_twoPointers(nums, target) == expected
