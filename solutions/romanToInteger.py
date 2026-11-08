# 13. Roman to Integer - https://leetcode.com/problems/roman-to-integer/description/

class Solution:
    def __init__(self):
        self.__roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    def romanToInt(self, s: str) -> int:
        answer = 0
        if s == "":
            return answer

        lastIndex = len(s) - 1
        answer = self.__roman.get(s[lastIndex])

        for c in range(lastIndex - 1, -1, -1):
            current = self.__roman.get(s[c])
            prev = self.__roman.get(s[c + 1])

            if current >= prev:
                answer += current
            else:
                answer -= current

        return answer
