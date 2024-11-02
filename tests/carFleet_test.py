import unittest
from solutions.carFleet import Solution

class SolutionTest(unittest.TestCase):
    def test(self):
        self.assertEqual(Solution().carFleet(12, [10,8,0,5,3], [2,4,1,1,3]), 3)