from solutions.reverseString import Solution


class TestReverseString:
    def test_example1(self):
        s = ["h", "e", "l", "l", "o"]
        Solution().reverseString(s)
        assert s == ["o", "l", "l", "e", "h"]

    def test_example2(self):
        s = ["H", "a", "n", "n", "a", "h"]
        Solution().reverseString(s)
        assert s == ["h", "a", "n", "n", "a", "H"]

    def test_empty(self):
        s = []
        Solution().reverseString(s)
        assert s == []

    def test_single(self):
        s = ["a"]
        Solution().reverseString(s)
        assert s == ["a"]

    def test_palindrome(self):
        s = ["r", "a", "c", "e", "c", "a", "r"]
        Solution().reverseString(s)
        assert s == ["r", "a", "c", "e", "c", "a", "r"]
