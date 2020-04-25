#contest url:https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/531/week-4/3308/

#referred from discussion section
import math
class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        if m == 0:
            return 0
        down = int(math.log(m, 2))
        up = int(math.log(n,2))
        if down!=up:
            return 0
        result = m
        for i in range (m+1, n+1):
            result = result & i
        return result