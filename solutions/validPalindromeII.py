# 680. Valid Palindrome II - https://leetcode.com/problems/valid-palindrome-ii/description/
class Solution:
    def validPalindrome(self, s: str) -> bool:
        length = len(s)
        left = 0
        right = length - 1

        while left < right:
            if s[left] != s[right]:
                return self.isPalindrome(s, left + 1, right) or self.isPalindrome(
                    s, left, right - 1
                )
            left += 1
            right -= 1

        return True

    def isPalindrome(self, s: str, left: int, right: int) -> bool:
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1

        return True
