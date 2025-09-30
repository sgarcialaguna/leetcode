from utils import Trie
import pytest


def longestCommonPrefix(strs: list[str]) -> str:
    t = Trie()
    for s in strs:
        t.insert(s)
    return t.get_common_prefix()


@pytest.mark.parametrize(
    "strs, expected",
    [(["flower", "flow", "flight"], "fl"), (["dog", "racecar", "car"], "")],
)
def test_longestCommonPrefix(strs, expected):
    assert longestCommonPrefix(strs) == expected
