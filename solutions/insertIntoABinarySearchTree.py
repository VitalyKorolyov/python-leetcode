# Definition for a binary tree node.
from typing import Optional


# 701. Insert into a Binary Search Tree - https://leetcode.com/problems/insert-into-a-binary-search-tree/description/
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root == None:
            return TreeNode(val)

        if root.val > val:
            root.left = self.insertIntoBST(root.left, val)
        else:
            root.right = self.insertIntoBST(root.right, val)

        return root

    def insertIntoBSTIterative(
        self, root: Optional[TreeNode], val: int
    ) -> Optional[TreeNode]:
        if root == None:
            return TreeNode(val)

        cur = root

        while True:
            if cur.val > val:
                if cur.left == None:
                    cur.left = TreeNode(val)
                    break
                cur = cur.left
            else:
                if cur.right == None:
                    cur.right = TreeNode(val)
                    break
                cur = cur.right

        return root
