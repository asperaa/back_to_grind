"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""516. Longest Palindromic Subsequence
"""

class Solution:

    def longestPalindromeSubseq(self, s):
        rev_s = s[::-1]
        m, n = len(s), len(rev_s)
        dp = [[None for _ in range(1+n)]for _ in range(1+m)]
        for i in range(m+1):
            dp[i][0] = 0
        for j in range(1, n+1):
            dp[0][j] = 0
        for i in range(1, m+1):
            for j in range(1, n+1):
                if s[i-1] == rev_s[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[m][n]