from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash = set(nums)
        res = 0

        for num in nums:
            if num - 1 not in hash:
                length = 1

                while (length + num) in hash:
                    length += 1
                
                res = max(res, length)

        return res