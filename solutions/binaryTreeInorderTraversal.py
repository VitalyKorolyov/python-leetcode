# Definition for a binary tree node.
from typing import List, Optional


# 94. Binary Tree Inorder Traversal - https://leetcode.com/problems/binary-tree-inorder-traversal/description/
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = list()
        self.dfs(root, result)
        return result

    def dfs(self, root: Optional[TreeNode], result: List[int]):
        if root is None:
            return

        self.dfs(root.left, result)
        result.append(root.val)
        self.dfs(root.right, result)
