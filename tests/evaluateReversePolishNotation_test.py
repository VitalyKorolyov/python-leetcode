from solutions.evaluateReversePolishNotation import Solution


class TestSolution:
    def test(self):
        assert Solution().evalRPN(["2", "1", "+", "3", "*"]) == 9
        assert Solution().evalRPN(["4", "13", "5", "/", "+"]) == 6
