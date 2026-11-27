from solutions.containsDuplicate import Solution


class TestSolution:
    def test(self):
        assert Solution().containsDuplicate([4, 3, 2, 4]) == True
        assert Solution().containsDuplicate([1, 2, 3, 4]) == False
        assert Solution().containsDuplicate([1, 2, 3, 4]) == False
