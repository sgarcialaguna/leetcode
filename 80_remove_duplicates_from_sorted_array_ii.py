from typing import List
import pytest


def removeDuplicatesII(nums: List[int]) -> int:
    j = 1
    count = 1

    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1]:
            count += 1
        else:
            count = 1

        if count <= 2:
            nums[j] = nums[i]
            j += 1

    return j


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
