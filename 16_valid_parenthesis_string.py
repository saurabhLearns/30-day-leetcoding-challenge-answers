#contest url: https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/530/week-3/3301/
class Solution:
    def checkValidString(self, s: str) -> bool:
        if not s: return True
        curve = s
        lower = 0
        higher = 0
        for i in curve:
            if i == '(':
                lower+=1
            else:
                lower-=1
            if i != ')':
                higher += 1
            else:
                higher -= 1
            if higher < 0:
                break
            lower = max (lower, 0)
            
        if lower == 0:
            return True 
        else:
            return False
           
       