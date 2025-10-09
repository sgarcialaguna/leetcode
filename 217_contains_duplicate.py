import pytest


def containsDuplicate(nums: list[int]) -> bool:
    """Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct."""

    # Using a dict here results in an even faster running time on Leetcode. Not sure why, time complexity should be the same.
    # Using a set for simplicity, we don't really need values
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)

    return False


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([1, 2, 3, 1], True),
        ([1, 2, 3, 4], False),
        ([1, 1, 1, 3, 3, 4, 3, 2, 4, 2], True),
        ([], False),
    ],
)
def test_containsDuplicate(nums, expected):
    assert containsDuplicate(nums) is expected
