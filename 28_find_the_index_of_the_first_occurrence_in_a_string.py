import pytest


# What I would actually do in real life
def strStr(haystack: str, needle: str) -> int:
    return haystack.find(needle)


def strStr_naive(haystack: str, needle: str) -> int:
    if not haystack or not needle:
        return -1

    if len(needle) > len(haystack):
        return -1

    for i in range(len(haystack) - len(needle) + 1):
        if haystack[i : i + len(needle)] == needle:
            return i

    return -1


# See https://en.wikipedia.org/wiki/Knuth%E2%80%93Morris%E2%80%93Pratt_algorithm for an optimized solution


@pytest.mark.parametrize(
    "haystack, needle, expected",
    [("sadbutsad", "sad", 0), ("leetcode", "leeto", -1), ("a", "a", 0)],
)
def test_convert(haystack, needle, expected):
    assert strStr(haystack, needle) == expected
    assert strStr_naive(haystack, needle) == expected
