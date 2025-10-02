import pytest


def twoSum(nums: list[int], target: int) -> list[int]:
    lookup = {}
    for i, num in enumerate(nums):
        lookup[num] = i

    for idx, num in enumerate(nums):
        if target - num in lookup and lookup[target - num] != idx:
            return [idx, lookup[target - num]]

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
