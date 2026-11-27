from solutions.TopKElementsInList import Solution


class TestSolution:
    def test(self):
        assert Solution().topKFrequent([1, 1, 1, 2, 2, 3], 2) == [1, 2]
        assert Solution().topKFrequent([7, 7], 1) == [7]
