import pytest


def candy(ratings: list[int]) -> int:
    candies = [1] * len(ratings)

    # loop forwards and backwards
    for i in range(1, len(candies)):
        if ratings[i] > ratings[i - 1]:
            candies[i] = candies[i - 1] + 1

    for i in range(len(candies) - 2, -1, -1):
        if ratings[i] > ratings[i + 1]:
            candies[i] = max(candies[i], candies[i + 1] + 1)

    return sum(candies)


@pytest.mark.parametrize(
    "ratings, expected",
    [([1, 0, 2], 5), ([1, 2, 2], 4), ([5, 4, 3, 2, 1], sum([5, 4, 3, 2, 1]))],
)
def test_candy(ratings, expected):
    assert candy(ratings) == expected
