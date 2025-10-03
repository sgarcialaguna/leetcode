import pytest


def binary_search(haystack: list[int], needle: int) -> int:
    lo = 0
    hi = len(haystack) - 1

    while lo <= hi:
        mid = (lo + hi) // 2
        val = haystack[mid]

        if val == needle:
            return mid

        if val < needle:
            lo += 1

        if val > needle:
            hi -= 1

    return -1


def threeSum(nums: list[int]) -> list[list[int]]:
    result = []
    nums = sorted(nums)
    for i in range(len(nums) - 2):
        for j in range(i + 1, len(nums) - 1):
            needle = -(nums[i] + nums[j])
            k = binary_search(nums[j + 1 :], needle)
            if k != -1:
                triplet = [nums[i], nums[j], nums[k + j + 1]]
                if triplet not in result:
                    result.append([nums[i], nums[j], nums[k + j + 1]])

    return result


@pytest.mark.parametrize(
    "haystack, needle, expected",
    [
        ([-4, -1, -1, 0, 1, 2], -4, 0),
        ([-4, -1, -1, 0, 1, 2], -0, 3),
        ([-4, -1, -1, 0, 1, 2], -5, -1),
    ],
)
def test_binarySearch(haystack: list[int], needle: int, expected: int):
    assert binary_search(haystack, needle) == expected


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
