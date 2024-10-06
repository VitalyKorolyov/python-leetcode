import unittest
from solutions.TopKElementsInList import Solution

class SolutionTest(unittest.TestCase):
    def test(self):
        self.assertEqual(Solution().topKFrequent([1,1,1,2,2,3], 2), [1,2])
        self.assertEqual(Solution().topKFrequent([7,7], 1), [7])