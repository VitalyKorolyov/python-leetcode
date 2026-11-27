from solutions.containerWithMostWater import Solution


class TestSolution:
    def test(self):
        assert Solution().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
        assert Solution().maxArea([1, 1]) == 1
