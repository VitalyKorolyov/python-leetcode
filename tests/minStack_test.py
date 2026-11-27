from solutions.minStack import MinStack


class TestSolution:
    def test(self):
        minStack = MinStack()
        minStack.push(-2)
        minStack.push(0)
        minStack.push(-3)

        assert minStack.getMin() == -3

        minStack.pop()
        minStack.top()

        assert minStack.getMin() == -2
