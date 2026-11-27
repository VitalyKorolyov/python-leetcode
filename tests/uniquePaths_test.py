from solutions.uniquePaths import Solution


class TestUniquePaths:
    def test_1x1(self):
        assert Solution().uniquePaths(1, 1) == 1

    def test_2x2(self):
        assert Solution().uniquePaths(2, 2) == 2

    def test_3x3(self):
        assert Solution().uniquePaths(3, 3) == 6

    def test_3x2(self):
        assert Solution().uniquePaths(3, 2) == 3

    def test_2x3(self):
        assert Solution().uniquePaths(2, 3) == 3

    def test_7x3(self):
        assert Solution().uniquePaths(7, 3) == 28

    def test_3x7(self):
        assert Solution().uniquePaths(3, 7) == 28

    def test_large(self):
        assert Solution().uniquePaths(10, 10) == 48620
