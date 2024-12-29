from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 226. Invert Binary Tree - https://leetcode.com/problems/invert-binary-tree/description/
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        savedLeft = root.left
        root.left = root.right
        root.right = savedLeft

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
