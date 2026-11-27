from solutions.twoSum2 import Solution


class TestSolution:
    def test(self):
        assert Solution().twoSum([2, 7, 11, 15], 9) == [1, 2]
        assert Solution().twoSum([2, 3, 4], 6) == [1, 3]
