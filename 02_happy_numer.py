#contest url: https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/528/week-1/3284/
#problem url: https://leetcode.com/problems/happy-number/


class Solution:
    def isHappy(self, n: int) -> bool:
        sqList  = []
        sq = 0
        dig = 0
        while True:
            #print(n)
            while n > 0:
                dig = n % 10
                sq = sq + (dig*dig)
                n = n//10
            if sq == 1:
                print("True")
                return True
            else:
                if sq in sqList:
                    print("False")
                    return False
                else:
                    sqList.append(sq)
                    n = sq
                    sq = 0
        