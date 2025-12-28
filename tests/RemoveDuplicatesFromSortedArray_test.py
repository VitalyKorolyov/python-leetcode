import unittest
from solutions.RemoveDuplicatesFromSortedArray import Solution


class SolutionTest(unittest.TestCase):
    def test_removeDuplicates(self):
        # Test case 1: Empty array
        nums = []
        result = Solution().removeDuplicates(nums)
        self.assertEqual(result, 0)
        self.assertEqual(nums, [])

        # Test case 2: Single element
        nums = [1]
        result = Solution().removeDuplicates(nums)
        self.assertEqual(result, 1)
        self.assertEqual(nums, [1])

        # Test case 3: No duplicates
        nums = [1, 2, 3]
        result = Solution().removeDuplicates(nums)
        self.assertEqual(result, 3)
        self.assertEqual(nums, [1, 2, 3])

        # Test case 4: With duplicates
        nums = [1, 1, 2]
        result = Solution().removeDuplicates(nums)
        self.assertEqual(result, 2)
        self.assertEqual(nums[:2], [1, 2])

        # Test case 5: All duplicates
        nums = [1, 1, 1]
        result = Solution().removeDuplicates(nums)
        self.assertEqual(result, 1)
        self.assertEqual(nums[:1], [1])

        # Test case 6: Negative numbers
        nums = [-1, 0, 0, 1, 1]
        result = Solution().removeDuplicates(nums)
        self.assertEqual(result, 3)
        self.assertEqual(nums[:3], [-1, 0, 1])

        # Test case 7: Multiple duplicates
        nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
        result = Solution().removeDuplicates(nums)
        self.assertEqual(result, 5)
        self.assertEqual(nums[:5], [0, 1, 2, 3, 4])
