"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""931. Minimum Falling Path Sum
"""

class Solution:
    
    def minFallingPathSum(self, grid):
        if not grid:
            return 0
        m, n = len(grid), len(grid[0])
        dp = [[float('inf')for _ in range(n+1)]for _ in range(m+1)]
        for j in range(n+1):
            dp[m][j] = 0
        dp[m][n] = 0
        ans = float('inf')
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if j == 0:
                    dp[i][j] = min(dp[i+1][j], dp[i+1][j+1]) + grid[i][j]
                else:
                    dp[i][j] = min(dp[i+1][j-1], dp[i+1][j], dp[i+1][j+1]) + grid[i][j]
                if i == 0:
                    ans = min(ans, dp[i][j])
        return ans