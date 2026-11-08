import pytest
from solutions.romanToInteger import Solution


class TestRomanToInt:
    def test_one(self):
        assert Solution().romanToInt("III") == 3

    def test_two(self):
        assert Solution().romanToInt("LVIII") == 58

    def test_three(self):
        assert Solution().romanToInt("MCMXCIV") == 1994


if __name__ == "__main__":
    pytest.main()
