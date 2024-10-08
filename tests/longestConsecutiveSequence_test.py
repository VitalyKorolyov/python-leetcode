import unittest
from solutions.longestConsecutiveSequence import Solution

class SolutionTest(unittest.TestCase):
    def test(self):
        self.assertEqual(Solution().longestConsecutive([100,4,200,1,3,2]), 4)
        self.assertEqual(Solution().longestConsecutive([0,3,7,2,5,8,4,6,0,1]), 9)