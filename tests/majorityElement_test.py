import unittest
from solutions.majorityElement import Solution


class SolutionTest(unittest.TestCase):
    def test_majority_element_single_element(self):
        """Test with a single element"""
        self.assertEqual(Solution().majorityElement([1]), 1)

    def test_majority_element_two_elements_same(self):
        """Test with two identical elements"""
        self.assertEqual(Solution().majorityElement([1, 1]), 1)

    def test_majority_element_two_elements_different(self):
        """Test with two different elements where first is majority"""
        self.assertEqual(Solution().majorityElement([1, 2]), 1)

    def test_majority_element_basic(self):
        """Test basic case with clear majority element"""
        self.assertEqual(Solution().majorityElement([3, 2, 3]), 3)

    def test_majority_element_multiple_occurrences(self):
        """Test with multiple occurrences of majority element"""
        self.assertEqual(Solution().majorityElement([2, 2, 1, 1, 1, 2, 2]), 2)

    def test_majority_element_barely_majority(self):
        """Test when majority element appears just over n/2 times"""
        self.assertEqual(Solution().majorityElement([1, 2, 3, 1, 1]), 1)

    def test_majority_element_all_same(self):
        """Test when all elements are the same"""
        self.assertEqual(Solution().majorityElement([5, 5, 5, 5]), 5)

    def test_majority_element_large_array(self):
        """Test with a large array"""
        arr = [1] * 5000 + [2] * 4999
        self.assertEqual(Solution().majorityElement(arr), 1)

    def test_majority_element_negative_numbers(self):
        """Test with negative numbers"""
        self.assertEqual(Solution().majorityElement([-1, -1, 1, 1, 1]), 1)

    def test_majority_element_mixed_negative_and_positive(self):
        """Test with mixed negative and positive numbers"""
        self.assertEqual(Solution().majorityElement([-1, -1, -1, 2, 3]), -1)

    def test_majority_element_zero_included(self):
        """Test with zero as one of the elements"""
        self.assertEqual(Solution().majorityElement([0, 0, 1, 1, 1]), 1)


if __name__ == '__main__':
    unittest.main()
