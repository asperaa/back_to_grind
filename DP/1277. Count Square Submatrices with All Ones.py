"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""1277. Count Square Submatrices with All Ones
"""

class Solution:
    
    def countSquares(self, grid):
        if not grid:
            return 0
        m, n = len(grid), len(grid[0])
        dp = grid
        summ = sum(dp[0])
        summ += sum([dp[i][0] for i in range(1, m)])
        for i in range(1, m):
            for j in range(1, n):
                if dp[i][j] == 1:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                    summ += dp[i][j]
        return summ