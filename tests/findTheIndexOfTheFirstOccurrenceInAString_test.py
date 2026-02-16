import unittest
from solutions.findTheIndexOfTheFirstOccurrenceInAString import Solution


class SolutionTest(unittest.TestCase):
    def test_first_occurrence_at_start(self):
        # Example 1: needle occurs at index 0
        self.assertEqual(Solution().strStr("sadbutsad", "sad"), 0)

    def test_needle_not_in_haystack(self):
        # Example 2: needle not found
        self.assertEqual(Solution().strStr("leetcode", "leeto"), -1)

    def test_multiple_occurrences_returns_first(self):
        # "sad" occurs at index 0 and 6, should return 0
        self.assertEqual(Solution().strStr("sadbutsad", "sad"), 0)

    def test_needle_at_end(self):
        # needle at the end of haystack
        self.assertEqual(Solution().strStr("hello", "lo"), 3)

    def test_needle_in_middle(self):
        # needle in the middle
        self.assertEqual(Solution().strStr("abcdef", "cde"), 2)

    def test_needle_equals_haystack(self):
        # needle equals entire haystack
        self.assertEqual(Solution().strStr("abc", "abc"), 0)

    def test_single_character_needle(self):
        # single character needle
        self.assertEqual(Solution().strStr("hello", "l"), 2)

    def test_single_character_not_found(self):
        # single character not found
        self.assertEqual(Solution().strStr("hello", "z"), -1)

    def test_needle_longer_than_haystack(self):
        # needle is longer than haystack
        self.assertEqual(Solution().strStr("abc", "abcdef"), -1)

    def test_empty_needle(self):
        # empty needle should return 0 (first position)
        self.assertEqual(Solution().strStr("hello", ""), 0)
