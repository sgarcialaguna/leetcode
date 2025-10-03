import pytest
import itertools


def threeSum(nums: list[int]) -> list[list[int]]:
    result = []
    for i, j, k in itertools.combinations(range(len(nums)), 3):
        if nums[i] + nums[j] + nums[k] == 0:
            triplet = sorted([nums[i], nums[j], nums[k]])
            if triplet not in result:
                result.append(triplet)

    return result


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
