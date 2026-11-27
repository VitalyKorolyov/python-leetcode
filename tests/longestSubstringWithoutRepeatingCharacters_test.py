from solutions.longestSubstringWithoutRepeatingCharacters import Solution


class TestSolution:
    def test(self):
        assert Solution().lengthOfLongestSubstring("abcabcbb") == 3
        assert Solution().lengthOfLongestSubstring("pwwkew") == 3
