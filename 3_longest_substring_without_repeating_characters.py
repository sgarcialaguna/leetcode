import pytest


def lengthOfLongestSubstring(s: str) -> int:
    charSet = set()
    start = 0
    result = 0

    for end in range(len(s)):
        while s[end] in charSet:
            charSet.remove(s[start])
            start += 1
        charSet.add(s[end])
        result = max(result, end - start + 1)

    return result


@pytest.mark.parametrize(
    "s, expected", [("abcabcbb", 3), ("bbbbb", 1), ("pwwkew", 3), ("jbpnbwwd", 4)]
)
def test_lengthOfLongestSubstring(s, expected):
    assert lengthOfLongestSubstring(s) == expected
