# 125. Valid Palindrome - https://leetcode.com/problems/valid-palindrome/description/
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1

        while l < r:
            if (s[l].isdigit() or s[l].isalpha()) != True:
                l += 1
                continue

            if (s[r].isdigit() or s[r].isalpha()) != True:
                r -= 1
                continue

            if s[l].lower() != s[r].lower():
                return False

            l += 1
            r -= 1

        return True
