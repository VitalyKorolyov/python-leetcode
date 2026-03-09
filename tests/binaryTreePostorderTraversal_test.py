import unittest
from solutions.binaryTreePostorderTraversal import Solution, TreeNode

class TestPostorderTraversal(unittest.TestCase):
    def build_tree(self, nodes):
        # Helper to build tree from list (None for empty)
        if not nodes:
            return None
        root = TreeNode(nodes[0])
        queue = [root]
        i = 1
        while queue and i < len(nodes):
            node = queue.pop(0)
            if node:
                if i < len(nodes):
                    node.left = TreeNode(nodes[i]) if nodes[i] is not None else None
                    queue.append(node.left)
                    i += 1
                if i < len(nodes):
                    node.right = TreeNode(nodes[i]) if nodes[i] is not None else None
                    queue.append(node.right)
                    i += 1
        return root

    def test_empty_tree(self):
        sol = Solution()
        self.assertEqual(sol.postorderTraversal(None), [])

    def test_single_node(self):
        sol = Solution()
        root = TreeNode(1)
        self.assertEqual(sol.postorderTraversal(root), [1])

    def test_left_right(self):
        sol = Solution()
        root = self.build_tree([1, 2, 3])
        # Tree:   1
        #        / \
        #       2   3
        # Postorder: [2, 3, 1]
        self.assertEqual(sol.postorderTraversal(root), [2, 3, 1])

    def test_complex_tree(self):
        sol = Solution()
        root = self.build_tree([1, None, 2, 3])
        # Tree:   1
        #          \
        #           2
        #          /
        #         3
        # Postorder: [3, 2, 1]
        self.assertEqual(sol.postorderTraversal(root), [3, 2, 1])

if __name__ == '__main__':
    unittest.main()
