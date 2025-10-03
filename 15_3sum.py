import pytest

# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
# such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.


def threeSum(nums: list[int]) -> list[list[int]]:
    result = []
    nums = sorted(nums)
    for i in range(len(nums) - 2):
        if nums[i] > 0:
            # sorted array, we already have positive numbers
            break

        # Do not reuse the same numbers
        if i > 0 and nums[i - 1] == nums[i]:
            continue

        lo = i + 1
        hi = len(nums) - 1
        val = nums[i]

        target = -val
        while lo < hi:
            if nums[lo] + nums[hi] > target:
                hi -= 1
            elif nums[lo] + nums[hi] < target:
                lo += 1
            else:
                result.append([val, nums[lo], nums[hi]])

                # Do not reuse the same numbers
                lo, hi = lo + 1, hi - 1
                while lo < hi and nums[lo] == nums[lo - 1]:
                    lo += 1
                while lo < hi and nums[hi] == nums[hi + 1]:
                    hi -= 1

    return result


# @pytest.mark.parametrize(
#     "haystack, needle, expected",
#     [
#         ([-4, -1, -1, 0, 1, 2], -4, 0),
#         ([-4, -1, -1, 0, 1, 2], -0, 3),
#         ([-4, -1, -1, 0, 1, 2], -5, -1),
#     ],
# )
# def test_binarySearch(haystack: list[int], needle: int, expected: int):
#     assert binary_search(haystack, needle) == expected


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([-1, 0, 1, 2, -1, -4], [[-1, 0, 1], [-1, -1, 2]]),
        ([0, 1, 1], []),
        ([0, 0, 0], [[0, 0, 0]]),
    ],
)
def test_threeSum(nums: list[int], expected: list[list[int]]):
    expected = sorted(expected)
    expected = [sorted(a) for a in expected]

    result = threeSum(nums)
    result = sorted(result)
    result = [sorted(a) for a in result]

    assert result == expected
