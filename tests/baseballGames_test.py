import unittest
from solutions.baseballGames import Solution


class TestBaseballGames(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        ops = ["1", "2", "+", "C", "5", "D"]
        self.assertEqual(self.sol.calPoints(ops), 18)

    def test_example2(self):
        ops = ["5", "D", "+", "C"]
        self.assertEqual(self.sol.calPoints(ops), 15)

    def test_all_integers(self):
        ops = ["3", "4", "5"]
        self.assertEqual(self.sol.calPoints(ops), 12)

    def test_multiple_c(self):
        ops = ["1", "C", "2", "C", "3", "C"]
        self.assertEqual(self.sol.calPoints(ops), 0)
