from typing import List


# 121. Best Time to Buy and Sell Stock - https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProxit = 0
        minPrise = prices[0]

        for p in prices:
            maxProxit = max(p - minPrise, maxProxit)
            minPrise = min(minPrise, p)

        return maxProxit
