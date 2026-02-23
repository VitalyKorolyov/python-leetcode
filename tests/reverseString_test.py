import unittest
from solutions.reverseString import Solution


class TestReverseString(unittest.TestCase):
    def test_example1(self):
        s = ["h", "e", "l", "l", "o"]
        Solution().reverseString(s)
        self.assertEqual(s, ["o", "l", "l", "e", "h"])

    def test_example2(self):
        s = ["H", "a", "n", "n", "a", "h"]
        Solution().reverseString(s)
        self.assertEqual(s, ["h", "a", "n", "n", "a", "H"])

    def test_empty(self):
        s = []
        Solution().reverseString(s)
        self.assertEqual(s, [])

    def test_single(self):
        s = ["a"]
        Solution().reverseString(s)
        self.assertEqual(s, ["a"])

    def test_palindrome(self):
        s = ["r", "a", "c", "e", "c", "a", "r"]
        Solution().reverseString(s)
        self.assertEqual(s, ["r", "a", "c", "e", "c", "a", "r"])
