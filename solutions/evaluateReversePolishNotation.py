from typing import List


# 150. Evaluate Reverse Polish Notation - https://leetcode.com/problems/evaluate-reverse-polish-notation/description/
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stackNum = []

        for t in tokens:
            if t == "+":
                stackNum.append(stackNum.pop() + stackNum.pop())
            elif t == "-":
                a, b = stackNum.pop(), stackNum.pop()
                stackNum.append(b - a)
            elif t == "*":
                stackNum.append(stackNum.pop() * stackNum.pop())
            elif t == "/":
                a, b = stackNum.pop(), stackNum.pop()
                stackNum.append(int(float(b) / a))
            else:
                stackNum.append(int(t))

        return stackNum[0]
