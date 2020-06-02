"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""174. Dungeon Game
"""

class Solution:

    def calculateMinimumHP(self, grid):
        if not grid:
            return 1
        m, n = len(grid), len(grid[0])
        dp = [[0 for _ in range(n)]for _ in range(m)]
        dp[m-1][n-1] = 1 if grid[m-1][n-1] > 0 else 1 - grid[m-1][n-1]
        for i in range(m-2, -1, -1):
            dp[i][n-1] = 1 if dp[i+1][n-1] - grid[i][n-1] < 1 else dp[i+1][n-1] - grid[i][n-1]
        for j in range(n-2, -1, -1):
            dp[m-1][j] = 1 if dp[m-1][j+1] - grid[m-1][j] < 1 else dp[m-1][j+1] - grid[m-1][j]
        for i in range(m-2, -1, -1):
            for j in range(n-2, -1, -1):
                dp[i][j] = min(dp[i+1][j], dp[i][j+1]) - grid[i][j]
                if dp[i][j] < 1:
                    dp[i][j] = 1
        return dp[0][0]