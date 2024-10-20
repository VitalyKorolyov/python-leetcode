import unittest
from solutions.containerWithMostWater import Solution


class SolutionTest(unittest.TestCase):
    def test(self):
        self.assertEqual(Solution().maxArea([1,8,6,2,5,4,8,3,7]), 49)
        self.assertEqual(Solution().maxArea([1,1]), 1)
