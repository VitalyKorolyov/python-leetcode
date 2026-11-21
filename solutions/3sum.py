# 15. 3Sum - https://leetcode.com/problems/3sum/description/
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()

        answer = []
        for i in range(0, len(nums) - 2):
            if nums[i] > 0:
                break

            if i > 0 and nums[i - 1] == nums[i]:
                continue

            two_sums = self.findTwoSum(nums, -nums[i], i + 1)
            for pair in two_sums:
                answer.append([nums[i]] + pair)

        return answer


    def findTwoSum(self, nums: list[int], target: int, startIndex: int) -> list[list[int]]:
        pairs = []

        n = len(nums) - 1
        left, right = startIndex, n

        while left < right:
            if left > startIndex and nums[left] == nums[left - 1]:
                left = left + 1
                continue

            if right < n and nums[right] == nums[right + 1]:
                right = right - 1
                continue

            currentSum = nums[left] + nums[right]
            if target == currentSum:
                pairs.append([nums[left], nums[right]])
                left += 1
                right -= 1
            elif target > currentSum:
                left = left + 1
            else:
                right = right - 1

        return pairs