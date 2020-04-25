#contest url: https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/531/week-4/3307/

#completed with help of hints and suggestions in question
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        add = 0
        hashmap = {}
        hashmap.update({0:1})
        for i in range(len(nums)):
            add+=nums[i]
            if (add - k) in hashmap:
                count+=hashmap.get(add-k)
            if add in hashmap:
                hashmap.update({add:hashmap.get(add)+1})
            else:
                hashmap.update({add:1})
        return count
