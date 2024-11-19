
"We are the captains of our ships, amd we stat 'till the end. We see our stories through."

"Only length of LCS."

class Solution:
    
    def longestCommonSubsequence(self, X, Y):
        m, n = len(X), len(Y)
        dp = [[None for _ in range(m+1)] for _ in range(n+1)]
        return self.lcs(X, Y, dp, m, n)
    
    def lcs(self, x, y, dp, m, n):
        if m == 0 or n == 0:
            return 0
        if dp[m][n]:
            return dp[m][n]
        
        if x[m-1] == [n-1]:
            dp[m][n] = 1 + self.lcs(x, y, dp, m-1, n-1)
            return dp[m][n]
        else:
            dp[m][n] = max(self.lcs(x, y, dp, m-1, n), self.lcs(x, y, dp, m, n-1))
            return dp[m][n]
        
