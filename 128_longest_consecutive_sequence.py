import pytest


def longestConsecutive(nums: list[int]) -> int:
    """Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

    You must write an algorithm that runs in O(n) time."""

    if not nums:
        return 0

    nums_set = set(nums)
    result = 1

    for num in nums_set:
        curr = num
        sequence_length = 1

        if curr - 1 in nums_set:
            continue

        while curr + 1 in nums_set:
            curr += 1
            sequence_length += 1
            result = max(result, sequence_length)

    return result


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([100, 4, 200, 1, 3, 2], 4),
        ([0, 3, 7, 2, 5, 8, 4, 6, 0, 1], 9),
        ([1, 0, 1, 2], 3),
    ],
)
def test_longestConsecutive(nums, expected):
    assert longestConsecutive(nums) == expected
