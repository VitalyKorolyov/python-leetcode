import unittest
from solutions.countGoodNodesInBinaryTree import Solution, TreeNode


class SolutionTest(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_single_node(self):
        root = TreeNode(1)
        self.assertEqual(self.solution.goodNodes(root), 1)

    def test_all_good_nodes(self):
        #      3
        #     / \
        #    3   3
        root = TreeNode(3, TreeNode(3), TreeNode(3))
        self.assertEqual(self.solution.goodNodes(root), 3)

    def test_no_good_nodes_except_root(self):
        #      5
        #     / \
        #    1   1
        root = TreeNode(5, TreeNode(1), TreeNode(1))
        self.assertEqual(self.solution.goodNodes(root), 1)

    def test_mixed_tree(self):
        #      3
        #     / \
        #    1   4
        #   /   / \
        #  3   1   5
        root = TreeNode(3)
        root.left = TreeNode(1, TreeNode(3))
        root.right = TreeNode(4, TreeNode(1), TreeNode(5))
        self.assertEqual(self.solution.goodNodes(root), 4)

    def test_left_skewed(self):
        #    2
        #   /
        #  2
        # /
        # 2
        root = TreeNode(2, TreeNode(2, TreeNode(2)))
        self.assertEqual(self.solution.goodNodes(root), 3)

    def test_right_skewed(self):
        # 1
        #  \
        #   2
        #    \
        #     3
        root = TreeNode(1, None, TreeNode(2, None, TreeNode(3)))
        self.assertEqual(self.solution.goodNodes(root), 3)

    def test_decreasing_values(self):
        #    5
        #   /
        #  4
        # /
        # 3
        root = TreeNode(5, TreeNode(4, TreeNode(3)))
        self.assertEqual(self.solution.goodNodes(root), 1)

    def test_complex_tree(self):
        #        8
        #       / \
        #      3   10
        #     / \    \
        #    1   6    14
        #       / \   /
        #      4   7 13
        root = TreeNode(8)
        root.left = TreeNode(3, TreeNode(1), TreeNode(6, TreeNode(4), TreeNode(7)))
        root.right = TreeNode(10, None, TreeNode(14, TreeNode(13)))
        self.assertEqual(self.solution.goodNodes(root), 3)
