"""We are the captains of our ships, and we stay 'till the end. We see our stories through. 
"""

"""712. Minimum ASCII Delete Sum for Two Strings
"""

class Solution:

    def minimumDeleteSum(self, text1, text2):
        m, n = len(text1), len(text2)
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = ord(text1[i-1]) + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i-1][j])
        return sum(map(ord, text1 + text2)) - 2 * dp[m][n] 