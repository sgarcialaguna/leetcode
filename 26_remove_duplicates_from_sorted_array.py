from typing import List
import pytest


def removeDuplicates(nums: List[int]) -> int:
    n = len(nums)
    j = 1

    for i in range(1, n):
        if nums[i] != nums[i - 1]:
            nums[j] = nums[i]
            j += 1

    return j


@pytest.mark.parametrize(
    "nums,expectedLength,expectedArr",
    [([1, 1, 2], 2, [1, 2]), ([0, 0, 1, 1, 1, 2, 2, 3, 3, 4], 5, [0, 1, 2, 3, 4])],
)
def test_removeElement(nums: List[int], expectedLength: int, expectedArr: List[int]):
    result = removeDuplicates(nums)
    assert nums[:expectedLength] == expectedArr
    assert result == expectedLength
