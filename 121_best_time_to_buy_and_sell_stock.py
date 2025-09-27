from typing import List
import pytest


def maxProfit(prices: List[int]) -> int:
    profit = 0
    for i, price in enumerate(prices):
        maxPrice = max(prices[i:])
        if maxPrice > price:
            profit = max(profit, maxPrice - price)

    return profit


@pytest.mark.parametrize(
    "arr, expected", [([7, 1, 5, 3, 6, 4], 5), ([7, 6, 4, 3, 1], 0)]
)
def test_maxProfit(arr: List[int], expected: int):
    assert maxProfit(arr) == expected
