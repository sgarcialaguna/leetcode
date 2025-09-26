from typing import List
import pytest


def removeDuplicatesII(nums: List[int]) -> int:
    i = 2
    k = len(nums) - 1
    while i <= k:
        if nums[i] == nums[i - 1] and nums[i] == nums[i - 2]:
            nums[i:] = nums[i + 1 :] + [nums[i]]
            k -= 1
        else:
            i += 1
    return i


@pytest.mark.parametrize(
    "nums,expectedLength,expectedArr",
    [
        ([1, 1, 1, 2, 2, 3], 5, [1, 1, 2, 2, 3]),
        ([0, 0, 1, 1, 1, 1, 2, 3, 3], 7, [0, 0, 1, 1, 2, 3, 3]),
        ([1, 1, 1], 2, [1, 1]),
    ],
)
def test_removeElement(nums: List[int], expectedLength: int, expectedArr: List[int]):
    result = removeDuplicatesII(nums)
    assert nums[:expectedLength] == expectedArr
    assert result == expectedLength
