from solutions.validAnagram import Solution


class TestSolution:
    def test(self):
        assert Solution().isAnagram("test", "test1") == False
        assert Solution().isAnagram("test", "etst") == True
        assert Solution().isAnagram("hashMap", "Mapahsh") == True
