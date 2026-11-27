from solutions.dailyTemperatures import Solution


class TestSolution:
    def test(self):
        assert Solution().dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]) == [
            1,
            1,
            4,
            2,
            1,
            1,
            0,
            0,
        ]
        assert Solution().dailyTemperatures([30, 40, 50, 60]) == [1, 1, 1, 0]
