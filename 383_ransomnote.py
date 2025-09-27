from typing import Counter
import pytest


def canConstruct(ransomNote: str, magazine: str):
    magazine_counter = Counter(magazine)
    ransomNote_counter = Counter(ransomNote)

    for letter, amount in ransomNote_counter.items():
        if magazine_counter.get(letter, 0) < amount:
            return False

    return True


@pytest.mark.parametrize(
    "ransomNote, magazine, expected",
    [("a", "b", False), ("aa", "ab", False), ("aa", "aab", True)],
)
def test_canConstruct(ransomNote: str, magazine: str, expected: bool):
    assert canConstruct(ransomNote, magazine) == expected
