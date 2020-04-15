#contest url : https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/528/week-1/3283/
#problem url : https://leetcode.com/problems/single-number/

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = nums[0]
        for i in range(1, len(nums)):
            res = res^ nums[i]
        return res
        