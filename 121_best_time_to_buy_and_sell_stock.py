from typing import List
import pytest


def maxProfit(prices: List[int]) -> int:
    profit = 0

    maxVal = prices[len(prices) - 1]
    for j in range(len(prices) - 1, 0, -1):
        maxVal = max(maxVal, prices[j])
        profit = max(profit, maxVal - prices[j - 1])

    return profit


@pytest.mark.parametrize(
    "arr, expected", [([7, 1, 5, 3, 6, 4], 5), ([7, 6, 4, 3, 1], 0), ([1, 2], 1)]
)
def test_maxProfit(arr: List[int], expected: int):
    assert maxProfit(arr) == expected
