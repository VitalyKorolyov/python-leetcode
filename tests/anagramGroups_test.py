from solutions.anagramGroups import Solution


class TestSolution:
    def test(self):
        assert Solution().groupAnagrams(
            ["act", "pots", "tops", "cat", "stop", "hat"]
        ) == [["act", "cat"], ["pots", "tops", "stop"], ["hat"]]
        assert Solution().groupAnagrams([""]) == [[""]]
        assert Solution().groupAnagrams(["a"]) == [["a"]]
