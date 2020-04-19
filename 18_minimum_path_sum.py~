# import sys
class Solution:
	def minPathSum(self, grid: List[List[int]]) -> int:

	# classis recursive solution studied in class, but time limit exceeds 
	#     def minPath (grid, m, n):
	#         if m >=len(grid) or n >= len(grid[0]):
	#             return sys.maxsize
	#         elif m==len(grid)-1 and n==len(grid[0])-1:
	#             return grid[m][n]
	#         else:
	#             return (grid[m][n] + min(minPath(grid, m+1 , n), minPath(grid, m,n+1)))
	#     return(minPath(grid, 0, 0))
	
	#apparantely this dynamic programing solution works, yes I had to google for this.
		if(grid == None or len(grid)==0):
			return 0
			
		cols = len(grid[0])
		rows = len(grid)

		dp = [[0 for i in range(cols)] for j in range(rows)]
		dp[0][0] = grid[0][0]
		for i in range(1, cols):
			dp[0][i] = dp[0][i-1] + grid[0][i]
		for j in range(1, rows):
			dp[j][0] = dp[j-1][0] + grid[j][0]
		for i in range (1, rows):
			for j in range (1 , cols):
				if(dp[i-1][j] > dp[i][j-1]):
					dp[i][j] = dp[i][j-1] + grid[i][j]
				else:
					dp[i][j] = dp[i-1][j] + grid[i][j]
					
		return dp[rows-1][cols-1];