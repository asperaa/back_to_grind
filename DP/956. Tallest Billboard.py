"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""956. Tallest Billboard
"""

class Solution:
    
    def tallestBillboard(self, rods):
        summ = sum(rods)
        n = len(rods)
        dp = [[float('-inf') for _ in range(2*summ + 1)]for _ in range(n+1)]
        dp[0][summ] = 0
        for i in range(1, n+1):
            for j in range(2*summ+1):
                if j - rods[i-1] >= 0 and dp[i][j-rods[i-1]] != float('-inf'):
                    dp[i][j] = max(dp[i][j], dp[i][j-rods[i-1]] + rods[i-1])
                if j + rods[i-1] <= 2 * summ and dp[i][j+rods[i-1]] != float('-inf'):
                    dp[i][j] = max(dp[i][j], dp[i][j+rods[i-1]])
                if dp[i-1][j] != float('-inf'):
                    dp[i][j] = max(dp[i][j], dp[i-1][j])
        return dp[n][summ]