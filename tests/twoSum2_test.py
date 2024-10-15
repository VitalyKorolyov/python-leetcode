import unittest
from solutions.twoSum2 import Solution

class SolutionTest(unittest.TestCase):
    def test(self):
        self.assertEqual(Solution().twoSum([2, 7, 11, 15], 9), [1, 2])
        self.assertEqual(Solution().twoSum([2, 3, 4], 6), [1, 3])