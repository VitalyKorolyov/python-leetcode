import unittest
from solutions.permutationInString import Solution


class SolutionTest(unittest.TestCase):
    def test(self):
        self.assertEqual(Solution().checkInclusion("abc", "lecabee"), True)
        self.assertEqual(Solution().checkInclusion("abc", "lecaabee"), False)
