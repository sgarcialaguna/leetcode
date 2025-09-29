import pytest


def canCompleteCircuit(gas: list[int], cost: list[int]) -> int:
    # If total cost exceeds total gas, no need to check
    if sum(cost) > sum(gas):
        return -1

    total = 0
    start = 0

    for i in range(len(gas)):
        total += gas[i] - cost[i]

        if total < 0:
            total = 0
            start = i + 1

    return start


@pytest.mark.parametrize(
    "gas, cost, output",
    [
        ([1, 2, 3, 4, 5], [3, 4, 5, 1, 2], 3),
        ([2, 3, 4], [3, 4, 3], -1),
        ([5, 8, 2, 8], [6, 5, 6, 6], 3),
    ],
)
def test_canCompleteCircuit(gas, cost, output):
    assert canCompleteCircuit(gas, cost) == output
