from solutions.binaryNumberWithAlternatingBits import Solution


class TestSolution:
    def test_examples(self):
        # Provided examples
        assert Solution().hasAlternatingBits(5)  # 101
        assert not Solution().hasAlternatingBits(7)  # 111
        assert not Solution().hasAlternatingBits(11)  # 1011

    def test_additional_cases(self):
        # small values and edge cases
        assert Solution().hasAlternatingBits(1)  # 1
        assert Solution().hasAlternatingBits(2)  # 10
        assert not Solution().hasAlternatingBits(3)  # 11
        assert not Solution().hasAlternatingBits(4)  # 100
        assert Solution().hasAlternatingBits(10)  # 1010
        assert not Solution().hasAlternatingBits(12)  # 1100

    def test_zero(self):
        # not strictly required by problem but should behave sensibly
        assert Solution().hasAlternatingBits(0)
