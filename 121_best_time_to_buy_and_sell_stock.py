from typing import List
import pytest


def maxProfit(prices: List[int]) -> int:
    max_profit = 0
    min_price = prices[0]

    for price in prices:
        min_price = min(price, min_price)
        max_profit = max(price - min_price, max_profit)

    return max_profit


@pytest.mark.parametrize(
    "arr, expected", [([7, 1, 5, 3, 6, 4], 5), ([7, 6, 4, 3, 1], 0), ([1, 2], 1)]
)
def test_maxProfit(arr: List[int], expected: int):
    assert maxProfit(arr) == expected
