import unittest
from solutions.rottingOranges import Solution

class SolutionTest(unittest.TestCase):
    def test(self):
        self.assertEqual(Solution().orangesRotting([[2,1,1],[0,1,1],[1,0,1]]), -1)
        self.assertEqual(Solution().orangesRotting([[2,1,1],[1,1,0],[0,1,1]]), 4)
        self.assertEqual(Solution().orangesRotting([[0,2]]), 0)