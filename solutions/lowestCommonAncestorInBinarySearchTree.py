# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 235. Lowest Common Ancestor of a Binary Search Tree - https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/description/
class Solution:
    def lowestCommonAncestor(
        self, root: TreeNode, p: TreeNode, q: TreeNode
    ) -> TreeNode:
        return self.dfs(root, p, q)

    def dfs(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if root == None:
            return None

        minV = min(p.val, q.val)
        maxV = max(p.val, q.val)

        if minV <= root.val and maxV >= root.val:
            return root

        result: TreeNode
        if minV > root.val:
            result = self.dfs(root.right, p, q)
        else:
            result = self.dfs(root.left, p, q)

        return result
