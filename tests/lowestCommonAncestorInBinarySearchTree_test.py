import unittest
from solutions.lowestCommonAncestorInBinarySearchTree import Solution, TreeNode


class TestLowestCommonAncestorInBinarySearchTree(unittest.TestCase):
    def setUp(self):
        # Construct the following BST:
        #        6
        #      /   \
        #     2     8
        #    / \   / \
        #   0   4 7   9
        #      / \
        #     3   5
        self.root = TreeNode(6)
        self.root.left = TreeNode(2)
        self.root.right = TreeNode(8)
        self.root.left.left = TreeNode(0)
        self.root.left.right = TreeNode(4)
        self.root.left.right.left = TreeNode(3)
        self.root.left.right.right = TreeNode(5)
        self.root.right.left = TreeNode(7)
        self.root.right.right = TreeNode(9)
        self.solution = Solution()

    def test_lca_left_subtree(self):
        p = self.root.left  # 2
        q = self.root.left.right  # 4
        lca = self.solution.lowestCommonAncestor(self.root, p, q)
        self.assertEqual(lca.val, 2)

    def test_lca_right_subtree(self):
        p = self.root.right.left  # 7
        q = self.root.right.right  # 9
        lca = self.solution.lowestCommonAncestor(self.root, p, q)
        self.assertEqual(lca.val, 8)

    def test_lca_root(self):
        p = self.root.left  # 2
        q = self.root.right  # 8
        lca = self.solution.lowestCommonAncestor(self.root, p, q)
        self.assertEqual(lca.val, 6)

    def test_lca_same_node(self):
        p = self.root.left.right  # 4
        q = self.root.left.right  # 4
        lca = self.solution.lowestCommonAncestor(self.root, p, q)
        self.assertEqual(lca.val, 4)


if __name__ == "__main__":
    unittest.main()
