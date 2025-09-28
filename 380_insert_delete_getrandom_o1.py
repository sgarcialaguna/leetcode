import random
from typing import Set


class RandomizedSet:
    def __init__(self):
        self._s: Set[int] = set()

    def insert(self, val: int) -> bool:
        ret = val not in self._s
        self._s.add(val)
        return ret

    def remove(self, val: int) -> bool:
        if val in self._s:
            self._s.remove(val)
            return True

        return False

    def getRandom(self) -> int:
        return random.choice(list(self._s))


def test_randomizedset():
    rs = RandomizedSet()

    assert rs.insert(1) is True
    assert rs._s == {1}

    assert rs.remove(2) is False
    assert rs._s == {1}

    assert rs.insert(2) is True
    assert rs._s == {1, 2}

    rand = rs.getRandom()
    assert rand == 1 or rand == 2

    assert rs.remove(1) is True
    assert rs._s == {2}

    assert rs.insert(2) is False
    assert rs._s == {2}

    assert rs.getRandom() == 2
