from solutions.validPalindromeII import Solution


class TestValidPalindromeII:
    def setup_method(self, method):
        self.sol = Solution()

    def test_palindrome(self):
        assert self.sol.validPalindrome("aca")
        assert self.sol.validPalindrome("abca")
        assert self.sol.validPalindrome("racecar")
        assert self.sol.validPalindrome("deeee")
        assert self.sol.validPalindrome("a")
        assert self.sol.validPalindrome("")

    def test_not_palindrome(self):
        assert not self.sol.validPalindrome("abbadc")
        assert not self.sol.validPalindrome("abcdef")
        assert not self.sol.validPalindrome("abc")
        assert not self.sol.validPalindrome("abcda")

    def test_edge_cases(self):
        assert self.sol.validPalindrome("ab")  # Remove one to get 'a' or 'b'
        assert self.sol.validPalindrome("aa")
        assert self.sol.validPalindrome("aba")
        assert self.sol.validPalindrome("abcba")
        assert not self.sol.validPalindrome("abcdeca")  # Needs more than one removal
