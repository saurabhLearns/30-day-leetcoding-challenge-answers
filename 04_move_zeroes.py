#contest url : https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/528/week-1/3286/

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nonZero = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[nonZero] = nums[nonZero], nums[i]
                nonZero+=1
        print(nums)