class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 1448. Count Good Nodes in Binary Tree - https://leetcode.com/problems/count-good-nodes-in-binary-tree/description/
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return self.countGoodNodes(root, root.val)

    # Preorder Traversal, Root -> Left -> Right
    def countGoodNodes(self, node: TreeNode, max_value: int) -> int:
        if node is None:
            return 0

        good: int = 1 if node.val >= max_value else 0

        max_value = max(max_value, node.val)

        left: int = self.countGoodNodes(node.left, max_value)
        right: int = self.countGoodNodes(node.right, max_value)

        return good + left + right
