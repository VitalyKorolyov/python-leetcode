import unittest
from solutions.minStack import MinStack


class SolutionTest(unittest.TestCase):
    def test(self):
        minStack = MinStack()
        minStack.push(-2)
        minStack.push(0)
        minStack.push(-3)

        self.assertEqual(minStack.getMin(), -3)

        minStack.pop()
        minStack.top()

        self.assertEqual(minStack.getMin(), -2)
