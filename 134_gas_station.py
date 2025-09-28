import pytest


def canCompleteCircuitFromPosition(gas: list[int], cost: list[int], i: int) -> bool:
    if gas[i] == 0:
        return False

    gasTank = 0
    n = len(gas)
    travelled = 0
    while travelled < n:
        gasTank += gas[i] - cost[i]
        if gasTank < 0:
            return False
        i = (i + 1) % n
        travelled += 1

    return gasTank >= 0


def canCompleteCircuit(gas: list[int], cost: list[int]) -> int:
    n = len(gas)
    for i in range(n):
        if canCompleteCircuitFromPosition(gas, cost, i):
            return i
    return -1


@pytest.mark.parametrize(
    "gas, cost, position, result",
    [
        ([1, 2, 3, 4, 5], [3, 4, 5, 1, 2], 0, False),
        ([1, 2, 3, 4, 5], [3, 4, 5, 1, 2], 1, False),
        ([1, 2, 3, 4, 5], [3, 4, 5, 1, 2], 2, False),
        ([1, 2, 3, 4, 5], [3, 4, 5, 1, 2], 3, True),
        ([1, 2, 3, 4, 5], [3, 4, 5, 1, 2], 4, False),
    ],
)
def test_canCompleteCircuitFromPostion(gas, cost, position, result):
    assert canCompleteCircuitFromPosition(gas, cost, position) == result


@pytest.mark.parametrize(
    "gas, cost, output",
    [([1, 2, 3, 4, 5], [3, 4, 5, 1, 2], 3), ([2, 3, 4], [3, 4, 3], -1)],
)
def test_canCompleteCircuit(gas, cost, output):
    assert canCompleteCircuit(gas, cost) == output
