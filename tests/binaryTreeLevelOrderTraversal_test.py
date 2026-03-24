import unittest
from solutions.binaryTreeLevelOrderTraversal import Solution, TreeNode


class TestBinaryTreeLevelOrderTraversal(unittest.TestCase):
    def build_tree(self, values):
        """
        Helper function to build a binary tree from a list of values (level order),
        where None indicates a missing node.
        """
        if not values:
            return None
        root = TreeNode(values[0])
        queue = [root]
        i = 1
        while queue and i < len(values):
            node = queue.pop(0)
            if node:
                if i < len(values):
                    left_val = values[i]
                    node.left = TreeNode(left_val) if left_val is not None else None
                    queue.append(node.left)
                    i += 1
                if i < len(values):
                    right_val = values[i]
                    node.right = TreeNode(right_val) if right_val is not None else None
                    queue.append(node.right)
                    i += 1
        return root

    def test_empty_tree(self):
        sol = Solution()
        self.assertEqual(sol.levelOrder(None), [])

    def test_single_node(self):
        sol = Solution()
        root = TreeNode(1)
        self.assertEqual(sol.levelOrder(root), [[1]])

    def test_complete_tree(self):
        sol = Solution()
        # Tree:     3
        #         /   \
        #        9    20
        #            /  \
        #           15   7
        vals = [3, 9, 20, None, None, 15, 7]
        root = self.build_tree(vals)
        self.assertEqual(sol.levelOrder(root), [[3], [9, 20], [15, 7]])

    def test_left_skewed_tree(self):
        sol = Solution()
        # Tree: 1 -> 2 -> 3 -> 4
        vals = [1, 2, None, 3, None, 4]
        root = self.build_tree(vals)
        self.assertEqual(sol.levelOrder(root), [[1], [2], [3], [4]])

    def test_right_skewed_tree(self):
        sol = Solution()
        # Tree: 1 -> 2 -> 3 -> 4 (all right children)
        vals = [1, None, 2, None, 3, None, 4]
        root = self.build_tree(vals)
        self.assertEqual(sol.levelOrder(root), [[1], [2], [3], [4]])

    def test_full_tree(self):
        sol = Solution()
        # Tree:      1
        #         /    \
        #        2      3
        #       / \    / \
        #      4   5  6   7
        vals = [1, 2, 3, 4, 5, 6, 7]
        root = self.build_tree(vals)
        self.assertEqual(sol.levelOrder(root), [[1], [2, 3], [4, 5, 6, 7]])


if __name__ == "__main__":
    unittest.main()
