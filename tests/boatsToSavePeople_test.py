import unittest
from solutions.boatsToSavePeople import Solution


class TestBoatsToSavePeople(unittest.TestCase):
    def setUp(self):
        self.solver = Solution()

    def test_example1(self):
        people = [5, 1, 4, 2]
        limit = 6
        self.assertEqual(self.solver.numRescueBoats(people, limit), 2)

    def test_all_fit_in_pairs(self):
        people = [1, 2, 2, 1]
        limit = 3
        self.assertEqual(self.solver.numRescueBoats(people, limit), 2)

    def test_each_needs_boat(self):
        people = [3, 3, 3, 3]
        limit = 3
        self.assertEqual(self.solver.numRescueBoats(people, limit), 4)

    def test_large_person(self):
        people = [5, 1, 7, 4]
        limit = 7
        self.assertEqual(self.solver.numRescueBoats(people, limit), 3)

    def test_empty(self):
        people = []
        limit = 5
        self.assertEqual(self.solver.numRescueBoats(people, limit), 0)

    def test_one_person(self):
        people = [2]
        limit = 3
        self.assertEqual(self.solver.numRescueBoats(people, limit), 1)
