from typing import List


# 881. Boats to Save People - https://leetcode.com/problems/boats-to-save-people/description/
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()

        left = 0
        right = len(people) - 1
        numBoats = 0

        while left <= right:
            capacity = limit - people[right]
            right -= 1
            numBoats += 1

            if left <= right and capacity >= people[left]:
                left += 1

        return numBoats
