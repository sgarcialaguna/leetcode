from typing import List
import pytest


def rotateArray(nums: List[int], k: int) -> None:
    k = k % len(nums)

    length = len(nums)

    nums[:] = [*nums[length - k :], *nums[: length - k]]


@pytest.mark.parametrize(
    "nums, k,expected",
    [
        ([3, 2, 3], 0, [3, 2, 3]),
        ([1, 2, 3, 4, 5, 6, 7], 3, [5, 6, 7, 1, 2, 3, 4]),
        ([-1, -100, 3, 99], 2, [3, 99, -1, -100]),
    ],
)
def test_majorityElement(nums: List[int], k: int, expected: List[int]):
    rotateArray(nums, k)
    assert nums == expected
