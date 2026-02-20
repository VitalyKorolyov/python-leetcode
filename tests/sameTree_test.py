import unittest
from solutions.sameTree import Solution, TreeNode


class SolutionTest(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_both_empty(self):
        self.assertTrue(self.solution.isSameTree(None, None))

    def test_one_empty(self):
        tree = TreeNode(1)
        self.assertFalse(self.solution.isSameTree(tree, None))
        self.assertFalse(self.solution.isSameTree(None, tree))

    def test_single_node_same(self):
        t1 = TreeNode(5)
        t2 = TreeNode(5)
        self.assertTrue(self.solution.isSameTree(t1, t2))

    def test_single_node_different_value(self):
        t1 = TreeNode(5)
        t2 = TreeNode(6)
        self.assertFalse(self.solution.isSameTree(t1, t2))

    def test_simple_structurally_same(self):
        #   1
        #  / \
        # 2   3
        t1 = TreeNode(1, TreeNode(2), TreeNode(3))
        t2 = TreeNode(1, TreeNode(2), TreeNode(3))
        self.assertTrue(self.solution.isSameTree(t1, t2))

    def test_simple_structurally_different(self):
        # t1:   1     t2:   1
        #      /           \
        #     2             2
        t1 = TreeNode(1, TreeNode(2))
        t2 = TreeNode(1, None, TreeNode(2))
        self.assertFalse(self.solution.isSameTree(t1, t2))

    def test_complex_same(self):
        #      4                4
        #     / \              / \
        #    2   7            2   7
        #   / \   \          / \   \
        #  1   3   9        1   3   9
        t1 = TreeNode(
            4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7, None, TreeNode(9))
        )
        t2 = TreeNode(
            4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7, None, TreeNode(9))
        )
        self.assertTrue(self.solution.isSameTree(t1, t2))

    def test_complex_different_values(self):
        t1 = TreeNode(
            4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7, None, TreeNode(9))
        )
        t2 = TreeNode(
            4,
            TreeNode(2, TreeNode(1), TreeNode(99)),  # different leaf
            TreeNode(7, None, TreeNode(9)),
        )
        self.assertFalse(self.solution.isSameTree(t1, t2))
