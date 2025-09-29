import pytest


def distanceFromPosition(gas: list[int], cost: list[int], i: int) -> int:
    gasTank = 0
    n = len(gas)
    travelled = 0
    while travelled < n:
        gasTank += gas[i] - cost[i]
        if gasTank < 0:
            return travelled
        i = (i + 1) % n
        travelled += 1

    return travelled


def canCompleteCircuit(gas: list[int], cost: list[int]) -> int:
    # Idea: if you can't travel from a to b, you can't get to b from any station between a and b
    i = 0
    while i < len(gas):
        distance = distanceFromPosition(gas, cost, i)
        if distance == len(gas):
            return i
        i += max(distance, 1)

    return -1


@pytest.mark.parametrize(
    "gas, cost, position, result",
    [
        ([1, 2, 3, 4, 5], [3, 4, 5, 1, 2], 0, 0),
        ([1, 2, 3, 4, 5], [3, 4, 5, 1, 2], 1, 0),
        ([1, 2, 3, 4, 5], [3, 4, 5, 1, 2], 2, 0),
        ([1, 2, 3, 4, 5], [3, 4, 5, 1, 2], 3, 5),
        ([1, 2, 3, 4, 5], [3, 4, 5, 1, 2], 4, 2),
        ([2, 3, 4], [3, 4, 3], 0, 0),
        ([2, 3, 4], [3, 4, 3], 1, 0),
        ([2, 3, 4], [3, 4, 3], 2, 2),
    ],
)
def test_distanceFromPosition(gas, cost, position, result):
    print(distanceFromPosition(gas, cost, position))
    assert distanceFromPosition(gas, cost, position) == result


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
