#contest url : https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/529/week-2/3298/
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        countArray = [-2 for i in range(2*(len(nums))+1)]
        countArray[len(nums)] = -1
        maxLen = 0
        count = 0
        for i in range(len(nums)):
            
            count = count + (-1 if nums[i] == 0 else 1)
            if (countArray[count+len(nums)]>= -1 ):
                maxLen = max(maxLen, i - countArray[count+len(nums)])
            else:
                countArray[count+len(nums)] = i
        return maxLen