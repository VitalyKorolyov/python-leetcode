import unittest
from solutions.validAnagram import Solution

class SolutionTest(unittest.TestCase):
    def test(self):
        self.assertEqual(Solution().isAnagram("test", "test1"), False)
        self.assertEqual(Solution().isAnagram("test", "etst"), True)
        self.assertEqual(Solution().isAnagram("hashMap", "Mapahsh"), True)
