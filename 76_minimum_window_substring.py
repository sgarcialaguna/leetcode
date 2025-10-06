from collections import Counter
import pytest


def minWindow(s: str, t: str) -> str:
    """Given two strings s and t of lengths m and n respectively, return the minimum window
    of s such that every character in t (including duplicates) is included in the window.
    If there is no such substring, return the empty string "".

    The testcases will be generated such that the answer is unique.
    """

    start = 0
    counter = Counter(t)
    result = ""

    for end in range(len(s)):
        if s[end] not in counter:
            continue

        counter[s[end]] -= 1

        # Do we have a solution with all characters?
        if all(v <= 0 for v in counter.values()):
            result = result or s[start : end + 1]
            # Ok, but do we have duplicate or irrelevant characters? If so, adjust start
            for i in range(start, end):
                char = s[i]

                # We can not remove this character, so break
                if char in t and counter[char] >= 0:
                    break

                # if character is not in t, we can remove it

                # if we have duplicate characters, the counter will be below 0, we can advance
                if counter[char] < 0:
                    counter[char] += 1

                start += 1
                result = (
                    result
                    if len(result) < len(s[start : end + 1])
                    else s[start : end + 1]
                )

    return result


@pytest.mark.parametrize(
    "s,t,expected",
    [
        ("ADOBECODEBANC", "ABC", "BANC"),
        ("a", "a", "a"),
        ("a", "aa", ""),
        ("ab", "b", "b"),
        ("cabwefgewcwaefgcf", "cae", "cwae"),
    ],
)
def test_minWindow(s, t, expected):
    assert minWindow(s, t) == expected
