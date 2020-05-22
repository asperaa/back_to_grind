"""Wee are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""1143. Longest Common Subsequence [Bottom Up]
"""

class Solution:

    def LongestCommonSubsequence(self, text1, text2):
        m, n = len(text1), len(text2)
        dp = [[None for _ in range(n+1)]for _ in range(m+1)]
        for i in range(m+1):
            dp[i][0] = 0
        for j in range(n+1):
            dp[0][j] = 0
        for i in range(1, m+1):
            for j in range(1, n+1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[m][n]

