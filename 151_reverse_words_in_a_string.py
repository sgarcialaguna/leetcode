import pytest


def reverseWords(s: str) -> str:
    words = s.strip().split(" ")
    words = [word for word in words if word]
    words.reverse()
    return " ".join(words)


@pytest.mark.parametrize(
    "s, expected",
    [
        ("the sky is blue", "blue is sky the"),
        ("  hello world  ", "world hello"),
        ("a good   example", "example good a"),
    ],
)
def test_reverseWords(s, expected):
    assert reverseWords(s) == expected
