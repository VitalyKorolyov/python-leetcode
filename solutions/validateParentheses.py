# 20. Valid Parentheses - https://leetcode.com/problems/valid-parentheses/description/
class Solution:
    map = {")": "(", "}": "{", "]": "["}

    def isValid(self, s: str) -> bool:
        stack = []

        for c in s:
            if c == "(" or c == "[" or c == "{":
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False

                top = stack.pop()
                if self.map[c] != top:
                    return False

        return len(stack) == 0
