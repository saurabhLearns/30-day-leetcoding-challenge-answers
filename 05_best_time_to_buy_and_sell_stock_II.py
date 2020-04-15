#contest url : https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/528/week-1/3287/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i =0
        profit = 0
        j = 0
        while i < len(prices)-1:
            if prices[i] < prices[i+1]:
                j = i+1
                while j<len(prices)-1 and prices[j] < prices[j+1]:
                    j+=1
                profit+=prices[j] - prices[i]
                i=j+1
            else:
                i+=1
            #print(profit)
        #print(profit)
        return (profit)