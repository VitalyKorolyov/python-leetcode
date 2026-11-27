from solutions.rangeSumQueryImmutable import NumArray


class TestNumArray:
    def test_sumRange(self):
        nums = [-2, 0, 3, -5, 2, -1]
        obj = NumArray(nums)
        assert obj.sumRange(0, 2) == 1  # -2 + 0 + 3
        assert obj.sumRange(2, 5) == -1  # 3 + (-5) + 2 + (-1)
        assert obj.sumRange(0, 5) == -3  # sum of all
        assert obj.sumRange(1, 3) == -2  # 0 + 3 + (-5)
        assert obj.sumRange(3, 3) == -5  # single element
