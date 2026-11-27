from solutions.binaryTreePreorderTraversal import Solution, TreeNode


class TestBinaryTreePreorderTraversal:
    def setup_method(self, method):
        self.solution = Solution()

    def build_tree(self, values):
        # Helper to build tree from list (None for empty)
        if not values:
            return None
        nodes = [TreeNode(val) if val is not None else None for val in values]
        kids = nodes[::-1]
        root = kids.pop()
        for node in nodes:
            if node:
                if kids:
                    node.left = kids.pop()
                if kids:
                    node.right = kids.pop()
        return root

    def test_empty_tree(self):
        assert self.solution.preorderTraversal(None) == []

    def test_single_node(self):
        root = TreeNode(1)
        assert self.solution.preorderTraversal(root) == [1]

    def test_left_skewed(self):
        root = TreeNode(1, TreeNode(2, TreeNode(3)))
        assert self.solution.preorderTraversal(root) == [1, 2, 3]

    def test_right_skewed(self):
        root = TreeNode(1, None, TreeNode(2, None, TreeNode(3)))
        assert self.solution.preorderTraversal(root) == [1, 2, 3]

    def test_balanced_tree(self):
        # Tree:    1
        #        /   \
        #       2     3
        #      / \   / \
        #     4   5 6   7
        root = TreeNode(
            1,
            TreeNode(2, TreeNode(4), TreeNode(5)),
            TreeNode(3, TreeNode(6), TreeNode(7)),
        )
        assert self.solution.preorderTraversal(root) == [1, 2, 4, 5, 3, 6, 7]
