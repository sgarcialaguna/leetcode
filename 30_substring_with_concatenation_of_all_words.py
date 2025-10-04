from collections import Counter
import pytest


def isValidStartingPoint(s: str, words: list[str], start: int):
    word_counter = Counter(words)
    word_length = len(words[0])
    for i in range(start, min(len(s), start + len(words) * word_length), word_length):
        word = s[i : i + word_length]
        try:
            word_counter[word] = word_counter[word] - 1
            if not word_counter[word]:
                del word_counter[word]
        except KeyError:
            return False

    return len(word_counter) == 0


def findSubstring(s: str, words: list[str]) -> list[int]:
    result = []
    l, r = 0, len(words[0])

    while r <= len(s):
        if s[l:r] in words:
            if isValidStartingPoint(s, words, l):
                result.append(l)
        l += 1
        r += 1

    return result


@pytest.mark.parametrize(
    "s, words, expected",
    [
        ("barfoothefoobarman", ["foo", "bar"], [0, 9]),
        ("wordgoodgoodgoodbestword", ["word", "good", "best", "word"], []),
        ("barfoofoobarthefoobarman", ["bar", "foo", "the"], [6, 9, 12]),
        ("a", ["a"], [0]),
        (
            "a" * 1000,
            ["a"] * 500,
            list(range(501)),
        ),
    ],
)
def test_findSubstring(s, words, expected):
    assert findSubstring(s, words) == expected
