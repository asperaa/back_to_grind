"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""1143. Longest Common Subsequence [Top Down]
"""

class Solution:

    def longestCommonSubsequence(self, text1, text2):
        m = len(text1)
        n = len(text2)
        dp = [[None for _ in range(n+1)]for _ in range(m+1)]
        return self.lcs_helper(text1, text2, m, n, dp)

    def lcs_helper(self, text1, text2, m, n, dp):
        if dp[m][n]:
            return dp[m][n]
        if m == 0 or n == 0:
            return 0
        if text1[m-1] == text2[n-1]:
            dp[m][n] = 1 + self.lcs_helper(text1, text2, m-1, n-1, dp)
        else:
            dp[m][n] = max(self.lcs_helper(text1, text2, m-1, n, dp), self.lcs_helper(text1, text2, m, n-1, dp))
        return dp[m][n]