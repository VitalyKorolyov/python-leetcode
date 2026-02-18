# 693. Binary Number with Alternating Bits - https://leetcode.com/problems/binary-number-with-alternating-bits/description/


class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        bits = bin(n)

        for i in range(len(bits) - 1):
            if bits[i] == bits[i + 1]:
                return False

        return True
