from solutions.numberOfIslands import Solution


class TestNumberOfIslands:
    def test_example_1(self):
        grid = [
            ["0", "1", "1", "1", "0"],
            ["0", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0"],
        ]
        assert Solution().numIslands(grid) == 1

    def test_all_water(self):
        grid = [["0", "0"], ["0", "0"]]
        assert Solution().numIslands(grid) == 0

    def test_all_land(self):
        grid = [["1", "1"], ["1", "1"]]
        assert Solution().numIslands(grid) == 1

    def test_multiple_islands(self):
        grid = [["1", "0", "1", "0"], ["0", "1", "0", "1"], ["1", "0", "1", "0"]]
        assert Solution().numIslands(grid) == 6

    def test_single_row(self):
        grid = [["1", "0", "1", "1", "0", "1"]]
        assert Solution().numIslands(grid) == 3

    def test_single_column(self):
        grid = [["1"], ["0"], ["1"], ["1"], ["0"], ["1"]]
        assert Solution().numIslands(grid) == 3
