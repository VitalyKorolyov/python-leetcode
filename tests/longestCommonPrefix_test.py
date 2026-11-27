from solutions.longestCommonPrefix import Solution


class TestLongestCommonPrefix:
    def test_example_1(self):
        assert Solution().longestCommonPrefix(["bat", "bag", "bank", "band"]) == "ba"

    def test_no_common_prefix(self):
        assert Solution().longestCommonPrefix(["dog", "racecar", "car"]) == ""

    def test_full_word_prefix(self):
        assert Solution().longestCommonPrefix(["flower", "flow", "flowing"]) == "flow"

    def test_single_string(self):
        assert Solution().longestCommonPrefix(["alone"]) == "alone"

    def test_empty_list(self):
        assert Solution().longestCommonPrefix([]) == ""

    def test_empty_string_in_list(self):
        assert Solution().longestCommonPrefix(["", "abc", "abd"]) == ""

    def test_all_empty_strings(self):
        assert Solution().longestCommonPrefix(["", "", ""]) == ""

    def test_identical_strings(self):
        assert (
            Solution().longestCommonPrefix(["repeat", "repeat", "repeat"]) == "repeat"
        )
