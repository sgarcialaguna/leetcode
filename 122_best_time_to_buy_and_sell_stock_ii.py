from typing import List
import pytest


def maxProfit(prices: List[int]) -> int:
    profit = 0

    for i in range(len(prices) - 1):
        if prices[i + 1] > prices[i]:
            # Buy
            profit += prices[i + 1] - prices[i]

    return profit


@pytest.mark.parametrize(
    "arr, expected",
    [([7, 1, 5, 3, 6, 4], 7), ([7, 6, 4, 3, 1], 0), ([1, 2, 3, 4, 5], 4)],
)
def test_maxProfit(arr: List[int], expected: int):
    assert maxProfit(arr) == expected
