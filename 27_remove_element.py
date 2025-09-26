from typing import List
import pytest


def removeElement(nums: List[int], val: int) -> int:
    result = 0
    i = 0
    j = len(nums) - 1
    while i <= j:
        if nums[i] == val:
            nums[i:] = nums[i + 1 :] + [nums[i]]
            j -= 1
        else:
            i += 1
            result += 1

    return result


@pytest.mark.parametrize(
    "arr,elementToRemove,expectedResult,expectedArr",
    [([3, 2, 2, 3], 3, 2, [2, 2]), ([0, 1, 2, 2, 3, 0, 4, 2], 2, 5, [0, 1, 3, 0, 4])],
)
def test_removeElement(
    arr: List[int], elementToRemove: int, expectedResult: int, expectedArr: List[int]
):
    result = removeElement(arr, elementToRemove)
    assert arr[: len(expectedArr)] == expectedArr
    assert result == expectedResult
