#contest url : https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/530/week-3/3300/
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        finalAns = [0] * len(nums)
        rightVal = 1
        finalAns[0] = 1
        for i in range(1, len(nums)):
            finalAns[i] = nums[i-1] * finalAns[i-1]
        for i in reversed(range(len(nums))):
            finalAns[i] = finalAns[i] * rightVal
            rightVal = rightVal * nums[i]
        return finalAns