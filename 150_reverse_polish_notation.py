from collections import deque
import math
import pytest


def evalRPN(tokens: list[str]) -> int:
    """You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

    Evaluate the expression. Return an integer that represents the value of the expression.

    Note that:

        The valid operators are '+', '-', '*', and '/'.
        Each operand may be an integer or another expression.
        The division between two integers always truncates toward zero.
        There will not be any division by zero.
        The input represents a valid arithmetic expression in a reverse polish notation.
        The answer and all the intermediate calculations can be represented in a 32-bit integer.
    """
    stack = deque()
    for token in tokens:
        match token:
            case "+":
                right, left = stack.pop(), stack.pop()
                stack.append(left + right)
            case "-":
                right, left = stack.pop(), stack.pop()
                stack.append(left - right)
            case "*":
                right, left = stack.pop(), stack.pop()
                stack.append(left * right)
            case "/":
                right, left = stack.pop(), stack.pop()
                # Truncates toward zero
                stack.append(int(left / right))
            case _:
                stack.append(int(token))
    return stack.pop()


@pytest.mark.parametrize(
    "tokens, expected",
    [
        (["1", "1", "+"], 2),
        (["2", "1", "+", "3", "*"], 9),
        (["4", "13", "5", "/", "+"], 6),
        (["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"], 22),
    ],
)
def test_evalRPN(tokens, expected):
    assert evalRPN(tokens) == expected
