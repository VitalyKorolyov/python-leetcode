import unittest
from solutions.evaluateReversePolishNotation import Solution


class SolutionTest(unittest.TestCase):
    def test(self):
        self.assertEqual(Solution().evalRPN(["2", "1", "+", "3", "*"]), 9)
        self.assertEqual(Solution().evalRPN(["4", "13", "5", "/", "+"]), 6)
