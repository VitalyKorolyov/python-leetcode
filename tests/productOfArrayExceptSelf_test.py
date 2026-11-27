from solutions.productOfArrayExceptSelf import Solution


class TestSolution:
    def test(self):
        assert Solution().productExceptSelf([1, 2, 3, 4]) == [24, 12, 8, 6]
