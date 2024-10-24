import unittest
from solutions.validateParentheses import Solution


class SolutionTest(unittest.TestCase):
    def test(self):
        self.assertEqual(Solution().isValid("()[]{}"), True)
        self.assertEqual(Solution().isValid("([])"), True)
        self.assertEqual(Solution().isValid("(]"), False)
