import unittest
from solutions.binarySearch import Solution


class SolutionTest(unittest.TestCase):
    def test(self):
        self.assertEqual(Solution().search([1, 2, 5, 8, 9], 8), 3)
        self.assertEqual(Solution().search([1, 2, 5, 8, 9], 0), -1)
