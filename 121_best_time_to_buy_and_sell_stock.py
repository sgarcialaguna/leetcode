from typing import List
import pytest


def maxProfit(prices: List[int]) -> int:
    profit = 0

    maxLookup = {}
    for j in range(len(prices) - 1, 0, -1):
        maxLookup[j] = max(maxLookup.get(j + 1, prices[j]), prices[j])
        profit = max(profit, maxLookup[j] - prices[j - 1])

    return profit


@pytest.mark.parametrize(
    "arr, expected", [([7, 1, 5, 3, 6, 4], 5), ([7, 6, 4, 3, 1], 0)]
)
def test_maxProfit(arr: List[int], expected: int):
    assert maxProfit(arr) == expected
