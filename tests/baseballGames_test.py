from solutions.baseballGames import Solution


class TestBaseballGames:
    def setup_method(self, method):
        self.sol = Solution()

    def test_example1(self):
        ops = ["1", "2", "+", "C", "5", "D"]
        assert self.sol.calPoints(ops) == 18

    def test_example2(self):
        ops = ["5", "D", "+", "C"]
        assert self.sol.calPoints(ops) == 15

    def test_all_integers(self):
        ops = ["3", "4", "5"]
        assert self.sol.calPoints(ops) == 12

    def test_multiple_c(self):
        ops = ["1", "C", "2", "C", "3", "C"]
        assert self.sol.calPoints(ops) == 0
