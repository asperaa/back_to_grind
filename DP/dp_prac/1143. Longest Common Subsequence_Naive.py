

class Solution:
    
    def longestCommonSubsequence(self, X, Y):
        m, n = len(X), len(Y)
        return self.lcs(X, Y, m, n)
    
    def lcs(self, x, y, m, n):
        if m == 0 or n == 0:
            return 0
        
        if x[m-1] == y[n-1]:
            return 1 + self.lcs(x, y, m-1, n-1)
        else:
            return max(self.lcs(x, y, m-1, n), self.lcs(x, y, m, n-1))
                