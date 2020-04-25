#contest url: https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/531/week-4/3310/

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        temp = len(nums) - 1
        for i in range (len(nums)-1, -1, -1):
            if nums[i] + i >=temp:
                temp = i
        
        return True if temp == 0 else False