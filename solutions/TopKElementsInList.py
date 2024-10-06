import heapq
from typing import List

# 347. Top K Frequent Elements - https://leetcode.com/problems/top-k-frequent-elements/
class Solution:
    def heapTopKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for num in nums:
            count[num] = count.get(num, 0) + 1

        heap = []
        for num in count.keys():
            heapq.heappush(heap, (count[num], num))
            if(len(heap) > k):
                heapq.heappop(heap)
        
        result = []
        for i in range(k):
            result.append(heapq.heappop(heap)[1])
        
        return result
    
    # Bucket sort
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:  
        freq = [[] for i in range(len(nums) + 1)]

        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        for num, cnt in count.items():
            freq[cnt].append(num)
        
        result = []

        for i in range(len(freq) - 1, 0, -1):
            if len(result) == k:
                    break

            for num in freq[i]:
                if len(result) == k:
                    break
                result.append(num)
        
        return result