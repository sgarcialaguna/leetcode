from collections import defaultdict
import pytest


def groupAnagrams(strs: list[str]) -> list[list[str]]:
    lookup = defaultdict(list[str])

    for s in strs:
        key = "".join(sorted(s))
        lookup[key].append(s)

    return list(lookup.values())


@pytest.mark.parametrize(
    "strs, expected",
    [
        ([""], [[""]]),
        (["a"], [["a"]]),
        (
            ["eat", "tea", "tan", "ate", "nat", "bat"],
            [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]],
        ),
    ],
)
def test_groupAnagrams(strs: list[str], expected: list[list[str]]):
    result = groupAnagrams(strs)
    assert len(result) == len(expected)

    unordered_result = [set(r) for r in result]
    unordered_expected = [set(e) for e in expected]

    for r in unordered_result:
        assert r in unordered_expected
