from solutions.validPalindrome import Solution


class TestSolution:
    def test(self):
        assert Solution().isPalindrome("A man, a plan, a canal: Panama") == True
        assert Solution().isPalindrome("race a car") == False
