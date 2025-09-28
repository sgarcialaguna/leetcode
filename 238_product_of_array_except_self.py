import pytest


def product(arr: list[int]) -> list[int]:
    # Compute products of all numbers to the left and right of each index
    larr = [1] * len(arr)
    rarr = [1] * len(arr)

    for i in range(1, len(arr)):
        larr[i] = larr[i - 1] * arr[i - 1]

    for i in range(len(arr) - 2, -1, -1):
        rarr[i] = rarr[i + 1] * arr[i + 1]

    return [rarr[i] * larr[i] for i in range(len(arr))]


@pytest.mark.parametrize(
    "arr, expected",
    [
        ([1, 2, 3, 4], [24, 12, 8, 6]),
        ([-1, 1, 0, -3, 3], [0, 0, 9, 0, 0]),
        ([0, 0, 1, 2, 3], [0, 0, 0, 0, 0]),
    ],
)
def test_hindex(arr, expected):
    assert product(arr) == expected
