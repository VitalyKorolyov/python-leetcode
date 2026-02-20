from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 100. Same Tree - https://leetcode.com/problems/same-tree/description/
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p == None and q != None:
            return False
        if p != None and q == None:
            return False

        if p == None and q == None:
            return True

        if p.val != q.val:
            return False

        leftResult = self.isSameTree(p.left, q.left)
        rightResult = self.isSameTree(p.right, q.right)

        return leftResult and rightResult
