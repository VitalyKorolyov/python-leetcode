from solutions.permutationInString import Solution


class TestSolution:
    def test(self):
        assert Solution().checkInclusion("abc", "lecabee") == True
        assert Solution().checkInclusion("abc", "lecaabee") == False
