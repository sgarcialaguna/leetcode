from typing import List
import pytest


def removeDuplicates(nums: List[int]) -> int:
    i = 0
    k = len(nums) - 1
    while i < k:
        if nums[i] == nums[i + 1]:
            nums[i:] = nums[i + 1 :] + [nums[i]]
            k -= 1
        else:
            i += 1
    return k + 1


@pytest.mark.parametrize(
    "nums,expectedLength,expectedArr",
    [([1, 1, 2], 2, [1, 2]), ([0, 0, 1, 1, 1, 2, 2, 3, 3, 4], 5, [0, 1, 2, 3, 4])],
)
def test_removeElement(nums: List[int], expectedLength: int, expectedArr: List[int]):
    result = removeDuplicates(nums)
    assert nums[:expectedLength] == expectedArr
    assert result == expectedLength
