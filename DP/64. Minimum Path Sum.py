"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""64. Minimum Path Sum
"""

class Solution:

    def minPathSum(self, grid):
        if not grid:
            return 0
        m, n = len(grid), len(grid[0])
        dp = [[0 for _ in range(n+1)]for _ in range(m+1)]
        for i in range(m+1):
            dp[i][n] = float('inf')
        for j in range(n+1):
            dp[m][j] = float('inf')
        dp[m][n-1] = dp[m-1][n] = 0
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                dp[i][j] = grid[i][j] + min(dp[i+1][j], dp[i][j+1])
        return dp[0][0]
