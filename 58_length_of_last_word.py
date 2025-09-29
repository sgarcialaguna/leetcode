import pytest


def lengthOfLastWord(s: str) -> int:
    words = [word for word in s.strip().split(" ")]
    return len(words[len(words) - 1])


@pytest.mark.parametrize(
    "s, expected",
    [
        ("Hello World", 5),
        ("   fly me   to   the moon  ", 4),
        ("luffy is still joyboy", 6),
    ],
)
def test_lengthOfLastWord(s, expected):
    assert lengthOfLastWord(s) == expected
