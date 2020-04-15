#contest url: https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/528/week-1/3285/

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currentMax = nums[0]
        totalMax = nums[0]
        for i in range(1,len(nums)):
            currentMax = currentMax + nums[i]
            if currentMax < nums[i]:
                currentMax = nums[i]
            if currentMax > totalMax:
                totalMax = currentMax
        return totalMax