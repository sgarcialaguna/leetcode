import string
import pytest


def isPalindrome(s: str) -> bool:
    s = s.lower()
    s = s.translate(
        {
            ord(c): ""
            for c in set(string.printable)
            - set(string.ascii_lowercase)
            - set(string.digits)
        }
    )
    for i in range(len(s) // 2):
        if s[i] != s[len(s) - 1 - i]:
            return False

    return True


@pytest.mark.parametrize(
    "s, expected",
    [("A man, a plan, a canal: Panama", True), ("race a car", False), (" ", True)],
)
def test_isPalindrome(s: str, expected: bool):
    assert isPalindrome(s) == expected
