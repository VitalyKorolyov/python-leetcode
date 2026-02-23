import unittest
from solutions.concatenationOfArray import Solution

class TestConcatenationOfArray(unittest.TestCase):
    def test_example1(self):
        nums = [1, 2, 1]
        expected = [1, 2, 1, 1, 2, 1]
        self.assertEqual(Solution().getConcatenation(nums), expected)

    def test_example2(self):
        nums = [1, 3, 2, 1]
        expected = [1, 3, 2, 1, 1, 3, 2, 1]
        self.assertEqual(Solution().getConcatenation(nums), expected)

    def test_empty(self):
        nums = []
        expected = []
        self.assertEqual(Solution().getConcatenation(nums), expected)

    def test_single_element(self):
        nums = [5]
        expected = [5, 5]
        self.assertEqual(Solution().getConcatenation(nums), expected)

    def test_large(self):
        nums = list(range(100))
        expected = nums + nums
        self.assertEqual(Solution().getConcatenation(nums), expected)
