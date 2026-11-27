from solutions.validateParentheses import Solution


class TestSolution:
    def test(self):
        assert Solution().isValid("()[]{}") == True
        assert Solution().isValid("[({}()[])]") == True
        assert Solution().isValid("[([])}") == False
