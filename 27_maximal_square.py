#contest url: https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/531/week-4/3312/

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0]) if rows>0 else 0
        maxsquare = 0
        for i in range (rows):
            for j in range(cols):
                if matrix[i][j] == '1':
                    squarelen = 1
                    flag = True
                    while squarelen + i < rows and squarelen + j < cols and flag:
                        for k in range(j, squarelen+j+1):
                            if matrix[i+squarelen][k] == '0':
                                flag = False
                                break
                            
                        for k in range(i, squarelen+i+1):
                            if matrix[k][j+squarelen] == '0':
                                flag = False
                                break
                        if flag:
                            squarelen+=1
                    
                    if maxsquare < squarelen:
                        maxsquare = squarelen
        return maxsquare*maxsquare                       
                        