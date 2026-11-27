from solutions.binarySearch import Solution


class TestSolution:
    def test(self):
        assert Solution().search([1, 2, 5, 8, 9], 8) == 3
        assert Solution().search([1, 2, 5, 8, 9], 0) == -1
