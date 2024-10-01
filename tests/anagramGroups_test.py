import unittest
from solutions.anagramGroups import Solution

class SolutionTest(unittest.TestCase):
    def test(self):
        self.assertListEqual(Solution().groupAnagrams(["act","pots","tops","cat","stop","hat"]), [["act", "cat"], ["pots", "tops", "stop"], ["hat"]])
        self.assertListEqual(Solution().groupAnagrams([""]), [[""]])
        self.assertListEqual(Solution().groupAnagrams(["a"]), [["a"]])