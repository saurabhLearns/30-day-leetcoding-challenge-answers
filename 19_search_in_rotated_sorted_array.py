#contest url: https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/530/week-3/3304/

#made me refer stackoverflow, smh
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def rec(nums, target, low, high):
            mid = (low+high) // 2
            #print(mid)
            if low>high:
                return -1
            if nums[mid] == target:
                return mid
            if nums[high] == target:
                return high
            if nums[low] == target:
                return low
            if nums[low] <= nums[mid]:
                if nums[mid] > target and nums[low] < target:
                    return rec(nums, target, low, mid-1)
                else:
                    return rec(nums, target, mid+1, high)
            else:
                if nums[mid] < target and nums[high] > target:
                    return rec(nums, target, mid+1, high)
                else:
                    return rec(nums, target, low, mid-1)
            return -1
                
        return (rec(nums, target, 0, len(nums)-1))