#contest url : https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/528/week-1/3289/

class Solution:
    def countElements(self, arr: List[int]) -> int:
        listsort = sorted(arr)
        i=0
        j=0
        count = 0
        while i < len(listsort):
            j=i+1
            while j<len(listsort):
                if(listsort[j] > listsort[i]+1):
                    break
                if (listsort[j] == listsort[i]+1):
                    #listsort.pop(j)
                    count+=1
                    break
                else:
                    j+=1
            listsort.pop(i)
        return count