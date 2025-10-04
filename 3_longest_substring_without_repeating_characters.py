import pytest


def lengthOfLongestSubstring(s: str) -> int:
    start = 0
    end = 0
    result = s[start : end + 1]

    while end < len(s):
        result = s[start : end + 1]

        # We already have duplicates
        if len(set(result)) != len(result):
            start += 1
            end += 1
            continue

        if end + 1 < len(s) and s[end + 1] not in result:
            # We can increase the substring's length
            end += 1
            result = s[start : end + 1]
            continue

        # We can't, slide one over
        start += 1
        end += 1

    return len(result)


@pytest.mark.parametrize(
    "s, expected", [("abcabcbb", 3), ("bbbbb", 1), ("pwwkew", 3), ("jbpnbwwd", 4)]
)
def test_lengthOfLongestSubstring(s, expected):
    assert lengthOfLongestSubstring(s) == expected
