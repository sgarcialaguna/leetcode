import pytest


def wordPattern(pattern: str, s: str) -> bool:
    words = s.split(" ")
    if len(pattern) != len(words):
        return False

    lookup = {}
    reverseLookup = {}

    for letter, word in zip(pattern, words):
        if letter in lookup and lookup[letter] != word:
            return False

        if word in reverseLookup and reverseLookup[word] != letter:
            return False

        lookup[letter] = word
        reverseLookup[word] = letter
    return True


@pytest.mark.parametrize(
    "pattern, s, expected",
    [
        ("abc", "foo bar", False),
        ("abba", "dog cat cat dog", True),
        ("abba", "dog cat cat fish", False),
        ("aaaa", "dog cat cat dog", False),
    ],
)
def test_wordPattern(pattern, s, expected):
    assert wordPattern(pattern, s) is expected
