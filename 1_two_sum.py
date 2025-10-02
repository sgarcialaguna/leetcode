from itertools import combinations
import pytest


def twoSum(nums: list[int], target: int) -> list[int]:
    c = combinations(range(len(nums)), 2)
    for [first_idx, second_idx] in c:
        if nums[first_idx] + nums[second_idx] == target:
            return [first_idx, second_idx]

    raise Exception("OH NOES")


@pytest.mark.parametrize(
    "nums, target, expected",
    [
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
        ([3, 3], 6, [0, 1]),
    ],
)
def test_twoSum(nums: list[int], target: int, expected: list[int]):
    assert twoSum(nums, target) == expected
