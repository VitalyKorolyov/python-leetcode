# Definition for a binary tree node.
from typing import List, Optional


# 144. Binary Tree Preorder Traversal - https://leetcode.com/problems/binary-tree-preorder-traversal/description/
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = list()
        self.dfs(root, result)
        return result
    
    def dfs(self, root: Optional[TreeNode], result: List[int]):
         if root == None:
             return
         
         result.append(root.val)
         self.dfs(root.left, result)
         self.dfs(root.right, result)
