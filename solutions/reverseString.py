from typing import List


# 344. Reverse String - https://leetcode.com/problems/reverse-string/description/
class Solution:
    def reverseString(self, s: List[str]) -> None:
        length = len(s)

        for i in range(int(length / 2)):
            current = s[i]
            s[i] = s[length - 1 - i]
            s[length - 1 - i] = current
