from collections import deque


class MinStack:
    """Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

    Implement the MinStack class:

    MinStack() initializes the stack object.
    void push(int val) pushes the element val onto the stack.
    void pop() removes the element on the top of the stack.
    int top() gets the top element of the stack.
    int getMin() retrieves the minimum element in the stack.

    You must implement a solution with O(1) time complexity for each function."""

    def __init__(self):
        self.stack = deque()
        self.minStack = deque()

    def push(self, val: int) -> None:
        self.stack.appendleft(val)

        if not self.minStack or val <= self.minStack[0]:
            self.minStack.appendleft(val)

    def pop(self) -> None:
        val = self.stack.popleft()
        if val == self.minStack[0]:
            self.minStack.popleft()

    def top(self) -> int:
        return self.stack[0]

    def getMin(self) -> int:
        return self.minStack[0]


def test_minStack():
    obj = MinStack()

    obj.push(-2)
    assert obj.top() == -2
    assert obj.getMin() == -2

    obj.push(0)
    assert obj.top() == 0
    assert obj.getMin() == -2

    obj.push(-3)
    assert obj.top() == -3
    assert obj.getMin() == -3

    obj.pop()
    assert obj.top() == 0
    assert obj.getMin() == -2
