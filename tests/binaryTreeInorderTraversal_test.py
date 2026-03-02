import unittest
from solutions.binaryTreeInorderTraversal import Solution, TreeNode


class TestBinaryTreeInorderTraversal(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_empty_tree(self):
        self.assertEqual(self.solution.inorderTraversal(None), [])

    def test_single_node(self):
        root = TreeNode(1)
        self.assertEqual(self.solution.inorderTraversal(root), [1])

    def test_left_skewed_tree(self):
        root = TreeNode(3, TreeNode(2, TreeNode(1)))
        self.assertEqual(self.solution.inorderTraversal(root), [1, 2, 3])

    def test_right_skewed_tree(self):
        root = TreeNode(1, None, TreeNode(2, None, TreeNode(3)))
        self.assertEqual(self.solution.inorderTraversal(root), [1, 2, 3])

    def test_balanced_tree(self):
        #      2
        #     / \
        #    1   3
        root = TreeNode(2, TreeNode(1), TreeNode(3))
        self.assertEqual(self.solution.inorderTraversal(root), [1, 2, 3])

    def test_complex_tree(self):
        #      4
        #     / \
        #    2   5
        #   / \
        #  1   3
        root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(5))
        self.assertEqual(self.solution.inorderTraversal(root), [1, 2, 3, 4, 5])
