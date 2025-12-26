from typing import List

# 303. Range Sum Query - Immutable - https://leetcode.com/problems/range-sum-query-immutable/description/?q=range+sum+query
class NumArray:
    def __init__(self, nums: List[int]):
        self.prefSum = []
        sum = 0
        for n in nums:
            sum += n
            self.prefSum.append(sum)

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.prefSum[right]
        return self.prefSum[right] - self.prefSum[left - 1]
