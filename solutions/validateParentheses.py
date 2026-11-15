# 20. Valid Parentheses - https://leetcode.com/problems/valid-parentheses/description/
class Solution:
    pairs = {")": "(", "]": "[", "}": "{"}

    def isValid(self, s: str) -> bool:
        stack = []

        for c in s:
            if c in "([{":
                stack.append(c)
            elif not stack or self.pairs[c] != stack.pop():
                return False

        return not stack