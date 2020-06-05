"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""221. Maximal Square
"""

class Solution:
    
    def maximalSquare(self, matrix):
        if not matrix:
            return 0
        m, n = len(matrix), len(matrix[0])
        dp = [[0 for _ in range(n+1)]for _ in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                dp[i][j] = int(matrix[i-1][j-1])
        maxx = dp[1][1]
        for i in range(1, m+1):
            for j in range(1, n+1):
                if dp[i][j] == 0:
                    dp[i][j] = 0
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                maxx = max(maxx, dp[i][j])
        return maxx * maxx