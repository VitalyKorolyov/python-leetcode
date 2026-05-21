import unittest
from solutions.RemoveNthNodeFromEndOfList import Solution, ListNode


class SolutionTest(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def helper_create_linked_list(self, values):
        """Helper function to create a linked list from a list of values"""
        if not values:
            return None
        head = ListNode(values[0])
        current = head
        for val in values[1:]:
            current.next = ListNode(val)
            current = current.next
        return head

    def helper_linked_list_to_list(self, node):
        """Helper function to convert a linked list to a Python list for easy comparison"""
        result = []
        current = node
        while current:
            result.append(current.val)
            current = current.next
        return result

    def test_remove_middle_node(self):
        """Test removing a node from the middle of the list"""
        head = self.helper_create_linked_list([1, 2, 3, 4, 5])
        # Remove 3rd node from the end (value 3)
        result = self.solution.removeNthFromEnd(head, 3)
        self.assertEqual(self.helper_linked_list_to_list(result), [1, 2, 4, 5])

    def test_remove_single_node_list(self):
        """Test removing the only node in a single-node list"""
        head = self.helper_create_linked_list([1])
        result = self.solution.removeNthFromEnd(head, 1)
        self.assertIsNone(result)

    def test_remove_last_node(self):
        """Test removing the last node (n=1)"""
        head = self.helper_create_linked_list([1, 2, 3])
        # Remove 1st node from the end (last node)
        result = self.solution.removeNthFromEnd(head, 1)
        self.assertEqual(self.helper_linked_list_to_list(result), [1, 2])

    def test_remove_first_node(self):
        """Test removing the first node (head)"""
        head = self.helper_create_linked_list([1, 2, 3])
        # Remove 3rd node from the end (first node)
        result = self.solution.removeNthFromEnd(head, 3)
        self.assertEqual(self.helper_linked_list_to_list(result), [2, 3])

    def test_remove_from_two_node_list_first(self):
        """Test removing the first node from a two-node list"""
        head = self.helper_create_linked_list([1, 2])
        result = self.solution.removeNthFromEnd(head, 2)
        self.assertEqual(self.helper_linked_list_to_list(result), [2])

    def test_remove_from_two_node_list_second(self):
        """Test removing the second node from a two-node list"""
        head = self.helper_create_linked_list([1, 2])
        result = self.solution.removeNthFromEnd(head, 1)
        self.assertEqual(self.helper_linked_list_to_list(result), [1])

    def test_remove_from_longer_list(self):
        """Test removing node from a longer list"""
        head = self.helper_create_linked_list([1, 2, 3, 4, 5, 6, 7])
        # Remove 4th node from end (value 4)
        result = self.solution.removeNthFromEnd(head, 4)
        self.assertEqual(self.helper_linked_list_to_list(result), [1, 2, 3, 5, 6, 7])

    def test_remove_second_from_end(self):
        """Test removing the second-to-last node (n=2)"""
        head = self.helper_create_linked_list([1, 2, 3, 4, 5])
        result = self.solution.removeNthFromEnd(head, 2)
        self.assertEqual(self.helper_linked_list_to_list(result), [1, 2, 3, 5])

    def test_preserve_list_structure(self):
        """Test that the remaining structure is properly maintained"""
        head = self.helper_create_linked_list([10, 20, 30, 40, 50])
        result = self.solution.removeNthFromEnd(head, 2)
        # Remove 40 (2nd from end)
        self.assertEqual(self.helper_linked_list_to_list(result), [10, 20, 30, 50])
        # Verify links are correct
        current = result
        self.assertEqual(current.val, 10)
        current = current.next
        self.assertEqual(current.val, 20)
        current = current.next
        self.assertEqual(current.val, 30)
        current = current.next
        self.assertEqual(current.val, 50)
        self.assertIsNone(current.next)

    def test_large_n_equals_list_length(self):
        """Test when n equals the length of the list (remove first node)"""
        head = self.helper_create_linked_list([1, 2, 3, 4])
        result = self.solution.removeNthFromEnd(head, 4)
        self.assertEqual(self.helper_linked_list_to_list(result), [2, 3, 4])

    def test_remove_node_with_duplicate_values(self):
        """Test removing from list with duplicate values"""
        head = self.helper_create_linked_list([1, 1, 1, 1, 1])
        result = self.solution.removeNthFromEnd(head, 3)
        self.assertEqual(self.helper_linked_list_to_list(result), [1, 1, 1, 1])


if __name__ == "__main__":
    unittest.main()
