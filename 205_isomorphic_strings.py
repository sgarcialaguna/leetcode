import pytest


def isIsomorphic(s: str, t: str) -> bool:
    lookup: dict[str, str] = {}
    reverse_lookup: dict[str, str] = {}

    for si, ti in zip(s, t):
        if si in lookup and lookup[si] != ti:
            return False
        if ti in reverse_lookup and reverse_lookup[ti] != si:
            return False
        lookup[si] = ti
        reverse_lookup[ti] = si

    return True


@pytest.mark.parametrize(
    "s,t,expected",
    [
        ("egg", "add", True),
        ("foo", "bar", False),
        ("paper", "title", True),
        ("badc", "baba", False),
    ],
)
def test_isIsomorphic(s, t, expected):
    assert isIsomorphic(s, t) is expected
