#contest url: https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/530/week-3/3302/	
#lol someone had exact similar solution other language.
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def checkNext(grid, r, c):
            if r<0 or c<0 or r>=len(grid) or c>=len(grid[0]) or grid[r][c]!="1":
                return
            grid[r][c] = 'x'
            checkNext(grid, r-1, c)
            checkNext(grid, r+1, c)
            checkNext(grid, r, c-1)
            checkNext(grid, r, c+1)
            
        if len(grid) == 0 or len(grid[0]) == 0:
            return 0
        count = 0
        for r in range (len(grid)):
            for c in range (len(grid[0])):
                if grid[r][c] == "1":
                    count+=1
                    checkNext(grid, r, c)
        return count
    
