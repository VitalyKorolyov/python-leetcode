import unittest
from solutions.binaryNumberWithAlternatingBits import Solution


class SolutionTest(unittest.TestCase):
    def test_examples(self):
        # Provided examples
        self.assertTrue(Solution().hasAlternatingBits(5))  # 101
        self.assertFalse(Solution().hasAlternatingBits(7))  # 111
        self.assertFalse(Solution().hasAlternatingBits(11))  # 1011

    def test_additional_cases(self):
        # small values and edge cases
        self.assertTrue(Solution().hasAlternatingBits(1))  # 1
        self.assertTrue(Solution().hasAlternatingBits(2))  # 10
        self.assertFalse(Solution().hasAlternatingBits(3))  # 11
        self.assertFalse(Solution().hasAlternatingBits(4))  # 100
        self.assertTrue(Solution().hasAlternatingBits(10))  # 1010
        self.assertFalse(Solution().hasAlternatingBits(12))  # 1100

    def test_zero(self):
        # not strictly required by problem but should behave sensibly
        self.assertTrue(Solution().hasAlternatingBits(0))
