import pytest


def isHappy(n: int) -> bool:
    """Write an algorithm to determine if a number n is happy.

    A happy number is a number defined by the following process:

    Starting with any positive integer, replace the number by the sum of the squares of its digits.
    Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
    Those numbers for which this process ends in 1 are happy.

    Return true if n is a happy number, and false if not."""

    seenNumbers = set()
    curr = n
    while True:
        nextNumber = 0
        while curr > 0:
            nextNumber += pow(curr % 10, 2)
            curr = curr // 10
        if nextNumber == 1:
            return True

        key = "".join(sorted(str(nextNumber))).replace("0", "")
        if key in seenNumbers:
            return False
        seenNumbers.add(key)
        curr = nextNumber


@pytest.mark.parametrize("n, expected", [(19, True), (2, False)])
def test_isHappy(n, expected):
    assert isHappy(n) is expected
