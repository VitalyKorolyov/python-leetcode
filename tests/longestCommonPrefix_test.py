import unittest
from solutions.longestCommonPrefix import Solution


class TestLongestCommonPrefix(unittest.TestCase):
    def test_example_1(self):
        self.assertEqual(
            Solution().longestCommonPrefix(["bat", "bag", "bank", "band"]), "ba"
        )

    def test_no_common_prefix(self):
        self.assertEqual(Solution().longestCommonPrefix(["dog", "racecar", "car"]), "")

    def test_full_word_prefix(self):
        self.assertEqual(
            Solution().longestCommonPrefix(["flower", "flow", "flowing"]), "flow"
        )

    def test_single_string(self):
        self.assertEqual(Solution().longestCommonPrefix(["alone"]), "alone")

    def test_empty_list(self):
        self.assertEqual(Solution().longestCommonPrefix([]), "")

    def test_empty_string_in_list(self):
        self.assertEqual(Solution().longestCommonPrefix(["", "abc", "abd"]), "")

    def test_all_empty_strings(self):
        self.assertEqual(Solution().longestCommonPrefix(["", "", ""]), "")

    def test_identical_strings(self):
        self.assertEqual(
            Solution().longestCommonPrefix(["repeat", "repeat", "repeat"]), "repeat"
        )


if __name__ == "__main__":
    unittest.main()
