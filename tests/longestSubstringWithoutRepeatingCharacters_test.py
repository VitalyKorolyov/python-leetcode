import unittest
from solutions.longestSubstringWithoutRepeatingCharacters import Solution

class SolutionTest(unittest.TestCase):
    def test(self):
        self.assertEqual(Solution().lengthOfLongestSubstring("abcabcbb"), 3)
        self.assertEqual(Solution().lengthOfLongestSubstring("pwwkew"), 3)