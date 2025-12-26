import unittest
from solutions.rangeSumQueryImmutable import NumArray


class NumArrayTest(unittest.TestCase):
    def test_sumRange(self):
        nums = [-2, 0, 3, -5, 2, -1]
        obj = NumArray(nums)
        self.assertEqual(obj.sumRange(0, 2), 1)  # -2 + 0 + 3
        self.assertEqual(obj.sumRange(2, 5), -1)  # 3 + (-5) + 2 + (-1)
        self.assertEqual(obj.sumRange(0, 5), -3)  # sum of all
        self.assertEqual(obj.sumRange(1, 3), -2)  # 0 + 3 + (-5)
        self.assertEqual(obj.sumRange(3, 3), -5)  # single element