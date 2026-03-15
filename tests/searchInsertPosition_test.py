import unittest
from solutions.searchInsertPosition import Solution


class TestSearchInsertPosition(unittest.TestCase):
    def test_example_1(self):
        nums = [-1, 0, 2, 4, 6, 8]
        target = 5
        expected = 4
        self.assertEqual(Solution().searchInsert(nums, target), expected)

    def test_target_found(self):
        nums = [1, 3, 5, 6]
        target = 5
        expected = 2
        self.assertEqual(Solution().searchInsert(nums, target), expected)

    def test_insert_at_end(self):
        nums = [1, 3, 5, 6]
        target = 7
        expected = 4
        self.assertEqual(Solution().searchInsert(nums, target), expected)

    def test_insert_at_start(self):
        nums = [1, 3, 5, 6]
        target = 0
        expected = 0
        self.assertEqual(Solution().searchInsert(nums, target), expected)

    def test_single_element(self):
        nums = [2]
        target = 1
        expected = 0
        self.assertEqual(Solution().searchInsert(nums, target), expected)
        target = 3
        expected = 1
        self.assertEqual(Solution().searchInsert(nums, target), expected)


if __name__ == "__main__":
    unittest.main()
