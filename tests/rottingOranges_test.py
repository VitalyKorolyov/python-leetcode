from solutions.rottingOranges import Solution


class TestSolution:
    def test(self):
        assert Solution().orangesRotting([[2, 1, 1], [0, 1, 1], [1, 0, 1]]) == -1
        assert Solution().orangesRotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]]) == 4
        assert Solution().orangesRotting([[0, 2]]) == 0
