import pytest


def summaryRanges(nums: list[int]) -> list[str]:
    """You are given a sorted unique integer array nums.

    A range [a,b] is the set of all integers from a to b (inclusive).

    Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.

    Each range [a,b] in the list should be output as:

    "a->b" if a != b
    "a" if a == b
    """
    if not nums:
        return []

    ranges = [[nums[0], nums[0]]]
    result = []
    currentRange = ranges[0]
    for i, num in enumerate(nums[: len(nums) - 1]):
        if nums[i + 1] == num + 1:
            currentRange[1] = num + 1
        else:
            currentRange = [nums[i + 1], nums[i + 1]]
            ranges.append(currentRange)

    for r in ranges:
        result.append(str(r[0]) if r[0] == r[1] else f"{r[0]}->{r[1]}")

    return result


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([], []),
        ([1], ["1"]),
        ([1, 2], (["1->2"])),
        ([1, 2, 4], ["1->2", "4"]),
        ([0, 1, 2, 4, 5, 7], ["0->2", "4->5", "7"]),
        ([0, 2, 3, 4, 6, 8, 9], ["0", "2->4", "6", "8->9"]),
    ],
)
def test_summaryRanges(nums, expected):
    assert summaryRanges(nums) == expected
