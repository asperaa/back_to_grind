# https://www.geeksforgeeks.org/problems/rod-cutting0840/1

class Solution:
    
    def cr(self, i, n, price, dp):
        if i==0:
            return n*price[0]
        if dp[i][n]:
            return dp[i][n]
        
        not_take = self.cr(i-1, n, price, dp)
        take = float('-inf')
        rod_length = i+1
        if rod_length <= n:
            take = price[i]+self.cr(i, n-rod_length, price, dp)
        dp[i][n] = max(take, not_take)
        return dp[i][n]
    
    
    def cutRod(self, price):
        n = len(price)
        dp = [[None for _ in range(n+1)]for _ in range(n)]
        return self.cr(n-1, n, price, dp)