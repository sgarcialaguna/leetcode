import pytest


def containsDuplicate(nums: list[int]) -> bool:
    """Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct."""
    if not nums:
        return False

    return len(set(nums)) != len(nums)


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
