from collections import Counter, defaultdict
import pytest


def containsNearbyDuplicate(nums: list[int], k: int) -> bool:
    """Given an integer array nums and an integer k, return true if there are two distinct indices i and j
    in the array such that nums[i] == nums[j] and abs(i - j) <= k."""

    lookup = defaultdict(list[int])

    for idx, num in enumerate(nums):
        arr = lookup[num]
        arr.append(idx)
        if len(arr) >= 2:
            if arr[len(arr) - 1] - arr[len(arr) - 2] <= k:
                return True

    return False


def containsNearbyDuplicateSlidingWindow(nums: list[int], k: int) -> bool:
    # See https://www.youtube.com/watch?v=ypn0aZ0nrL4
    window = set()
    L = 0

    for R in range(len(nums)):
        if R - L > k:
            window.remove(nums[L])
            L += 1

        if nums[R] in window:
            return True

        window.add(nums[R])

    return False


@pytest.mark.parametrize(
    "nums, k, expected",
    [
        ([], 10, False),
        ([1], 1, False),
        ([1, 2, 3, 1], 3, True),
        ([1, 0, 1, 1], 1, True),
        ([1, 2, 3, 1, 2, 3], 2, False),
    ],
)
def test_containsNearbyDuplicate(nums, k, expected):
    assert containsNearbyDuplicate(nums, k) is expected
    assert containsNearbyDuplicateSlidingWindow(nums, k) is expected
