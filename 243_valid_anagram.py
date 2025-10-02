from collections import Counter
import pytest


def isAnagram(s: str, t: str) -> bool:
    counter_s = Counter(s)
    counter_t = Counter(t)

    return counter_s == counter_t


@pytest.mark.parametrize(
    "s,t,expected", [("anagram", "nagaram", True), ("rat", "car", False)]
)
def test_isAnagram(s, t, expected):
    assert isAnagram(s, t) is expected
