import pytest
from collections import deque

bracketLookup = {")": "(", "}": "{", "]": "["}


def isValid(s: str) -> bool:
    """Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

    An input string is valid if:

    - Open brackets must be closed by the same type of brackets.
    - Open brackets must be closed in the correct order.
    - Every close bracket has a corresponding open bracket of the same type.
    """

    stack = deque()
    for char in s:
        if char in ["(", "{", "["]:
            stack.appendleft(char)
        else:
            if len(stack) == 0:
                return False
            openingBracket = stack.popleft()
            if openingBracket != bracketLookup[char]:
                return False

    return len(stack) == 0


@pytest.mark.parametrize(
    "s, expected",
    [
        ("()", True),
        ("(}", False),
        ("()[]{}", True),
        ("(]", False),
        ("([])", True),
        ("([)])", False),
    ],
)
def test_isValid(s, expected):
    assert isValid(s) is expected
