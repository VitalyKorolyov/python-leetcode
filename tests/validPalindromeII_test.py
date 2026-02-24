import unittest
from solutions.validPalindromeII import Solution

class TestValidPalindromeII(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_palindrome(self):
        self.assertTrue(self.sol.validPalindrome("aca"))
        self.assertTrue(self.sol.validPalindrome("abca"))
        self.assertTrue(self.sol.validPalindrome("racecar"))
        self.assertTrue(self.sol.validPalindrome("deeee"))
        self.assertTrue(self.sol.validPalindrome("a"))
        self.assertTrue(self.sol.validPalindrome(""))

    def test_not_palindrome(self):
        self.assertFalse(self.sol.validPalindrome("abbadc"))
        self.assertFalse(self.sol.validPalindrome("abcdef"))
        self.assertFalse(self.sol.validPalindrome("abc"))
        self.assertFalse(self.sol.validPalindrome("abcda"))

    def test_edge_cases(self):
        self.assertTrue(self.sol.validPalindrome("ab"))  # Remove one to get 'a' or 'b'
        self.assertTrue(self.sol.validPalindrome("aa"))
        self.assertTrue(self.sol.validPalindrome("aba"))
        self.assertTrue(self.sol.validPalindrome("abcba"))
        self.assertFalse(self.sol.validPalindrome("abcdeca"))  # Needs more than one removal

if __name__ == "__main__":
    unittest.main()
