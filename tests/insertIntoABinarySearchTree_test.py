import unittest
from solutions.insertIntoABinarySearchTree import Solution, TreeNode


def tree_to_list(root):
    if not root:
        return []
    result = []
    queue = [root]
    while queue:
        node = queue.pop(0)
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    # Remove trailing None values
    while result and result[-1] is None:
        result.pop()
    return result


class TestInsertIntoBST(unittest.TestCase):
    def test_insert_into_empty(self):
        sol = Solution()
        root = None
        val = 5
        new_root = sol.insertIntoBST(root, val)
        self.assertEqual(tree_to_list(new_root), [5])

    def test_insert_left_and_right(self):
        sol = Solution()
        root = TreeNode(4, TreeNode(2), TreeNode(7))
        val = 5
        new_root = sol.insertIntoBST(root, val)
        self.assertEqual(tree_to_list(new_root), [4, 2, 7, None, None, 5])

    def test_insert_deep(self):
        sol = Solution()
        root = TreeNode(
            40,
            TreeNode(20, TreeNode(10), TreeNode(30)),
            TreeNode(60, TreeNode(50), TreeNode(70)),
        )
        val = 25
        new_root = sol.insertIntoBST(root, val)
        self.assertIn(25, tree_to_list(new_root))

    def test_insert_into_empty_iterative(self):
        sol = Solution()
        root = None
        val = 5
        new_root = sol.insertIntoBSTIterative(root, val)
        self.assertEqual(tree_to_list(new_root), [5])

    def test_insert_left_and_right_iterative(self):
        sol = Solution()
        root = TreeNode(4, TreeNode(2), TreeNode(7))
        val = 5
        new_root = sol.insertIntoBSTIterative(root, val)
        self.assertEqual(tree_to_list(new_root), [4, 2, 7, None, None, 5])

    def test_insert_deep_iterative(self):
        sol = Solution()
        root = TreeNode(
            40,
            TreeNode(20, TreeNode(10), TreeNode(30)),
            TreeNode(60, TreeNode(50), TreeNode(70)),
        )
        val = 25
        new_root = sol.insertIntoBSTIterative(root, val)
        self.assertIn(25, tree_to_list(new_root))


if __name__ == "__main__":
    unittest.main()
