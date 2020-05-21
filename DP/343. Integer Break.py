"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""343. Integer Break
"""

class Solution:

    def integerBreak(self, n):
        weight = [i for i in range(1, n)]
        dp = [[None for _ in range(n+1)]for _ in range(len(weight)+1)]
        for j in range(n+1):
            dp[0][j] = 0
        for i in range(1, len(weight)+1):
            dp[i][0] = 1
        for i in range(1, len(weight)+1):
            for j in range(1, n+1):
                if j >= weight[i-1]:
                    dp[i][j] = max(weight[i-1] * dp[i][j-weight[i-1]], dp[i-1][j])
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[n-1][n]  