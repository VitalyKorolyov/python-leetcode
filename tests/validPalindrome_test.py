import unittest
from solutions.validPalindrome import Solution


class SolutionTest(unittest.TestCase):
    def test(self):
        self.assertEqual(
            Solution().isPalindrome("A man, a plan, a canal: Panama"), True
        )
        self.assertEqual(Solution().isPalindrome("race a car"), False)
