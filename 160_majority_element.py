from typing import List
import pytest


def majorityElement(nums: List[int]) -> int:
    # Boyer-Moore majority vote algorithm, see
    # https://en.wikipedia.org/wiki/Boyer%E2%80%93Moore_majority_vote_algorithm
    candidate = None
    counter = 0

    for num in nums:
        if counter == 0:
            candidate = num
            counter = 1
            continue

        if candidate == num:
            counter += 1
        else:
            counter -= 1

    return candidate


@pytest.mark.parametrize("nums,expected", [([3, 2, 3], 3), ([2, 2, 1, 1, 1, 2, 2], 2)])
def test_majorityElement(nums: List[int], expected: int):
    assert majorityElement(nums) == expected
