import unittest
from solutions.minimumSizeSubarraySum import Solution


class TestMinimumSizeSubarraySum(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        target = 10
        nums = [2, 1, 5, 1, 5, 3]
        self.assertEqual(self.sol.minSubArrayLen(target, nums), 3)

    def test_example2(self):
        target = 5
        nums = [1, 2, 1]
        self.assertEqual(self.sol.minSubArrayLen(target, nums), 0)

    def test_entire_array(self):
        target = 15
        nums = [1, 2, 3, 4, 5]
        self.assertEqual(self.sol.minSubArrayLen(target, nums), 5)

    def test_single_element(self):
        target = 3
        nums = [1, 2, 3, 4, 5]
        self.assertEqual(self.sol.minSubArrayLen(target, nums), 1)

    def test_no_subarray(self):
        target = 100
        nums = [1, 2, 3, 4, 5]
        self.assertEqual(self.sol.minSubArrayLen(target, nums), 0)

    def test_multiple_possible(self):
        target = 7
        nums = [2, 3, 1, 2, 4, 3]
        self.assertEqual(self.sol.minSubArrayLen(target, nums), 2)
