from solutions.carFleet import Solution


class TestSolution:
    def test(self):
        assert Solution().carFleet(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]) == 3
