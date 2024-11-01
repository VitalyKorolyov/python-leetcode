import unittest
from solutions.dailyTemperatures import Solution

class SolutionTest(unittest.TestCase):
    def test(self):
        self.assertEqual(Solution().dailyTemperatures([73,74,75,71,69,72,76,73]), [1,1,4,2,1,1,0,0])
        self.assertEqual(Solution().dailyTemperatures([30,40,50,60]), [1,1,1,0])