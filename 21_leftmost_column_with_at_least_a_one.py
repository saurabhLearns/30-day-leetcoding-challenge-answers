#contest url:https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/530/week-3/3306/

# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, x: int, y: int) -> int:
#    def dimensions(self) -> list[]:


#thanks, discussions
class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        row, col = binaryMatrix.dimensions()
        result = -1
        for i in range(row):
            start = 0
            end = col -1
            while start < end:
                mid = start + (end - start) // 2
                if binaryMatrix.get(i, mid) == 0:
                    start = mid+1
                else:
                    end = mid
            if(binaryMatrix.get(i, end) != 0):
                result = (end if result == -1 else min (result, end))
        return result
                
        # found = 0
        # start = 0
        # end = col        
        # while start <= end:
        #     mid = start+(end-start)//2
        #     i = 0
        #     flag = 0
        #     while i < row:
        #         if binaryMatrix.get(i, mid):
        #             flag = 1
        #             break
        #         else:
        #             i+=1
        #     if flag == 0:
        #         start = mid+1
        #     else:
        #         end = mid
        #         found = 1
        # if found:
        #     return start
        # else:
        #     return -1