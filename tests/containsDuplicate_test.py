import unittest
from solutions.containsDuplicate import Solution

class SolutionTest(unittest.TestCase):
    def test(self):
        self.assertEqual(Solution().containsDuplicate([4, 3, 2, 4]), True)
        self.assertEqual(Solution().containsDuplicate([1, 2, 3, 4]), False)
        self.assertEqual(Solution().containsDuplicate([1, 2, 3, 4]), False)