import pytest


def minSubArrayLen(target: int, nums: list[int]) -> int:
    if sum(nums) < target:
        return 0

    left, total = 0, 0
    result = len(nums)

    for right in range(len(nums)):
        total += nums[right]
        while total >= target:
            result = min(right - left + 1, result)
            total -= nums[left]
            left += 1

    return result


@pytest.mark.parametrize(
    "target, nums, expected",
    [(7, [2, 3, 1, 2, 4, 3], 2), (4, [1, 1, 4], 1), (11, [1] * 8, 0)],
)
def test_minSubArrayLen(target, nums, expected):
    assert minSubArrayLen(target, nums) == expected
