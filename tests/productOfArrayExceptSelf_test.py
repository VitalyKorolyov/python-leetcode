import unittest
from solutions.productOfArrayExceptSelf import Solution

class SolutionTest(unittest.TestCase):
    def test(self):
        self.assertEqual(Solution().productExceptSelf([1,2,3,4]), [24,12,8,6])
