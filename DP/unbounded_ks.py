# https://www.geeksforgeeks.org/problems/knapsack-with-duplicate-items4201/1

class Solution:
    
    def ks(self, i, capacity, val, wt, dp):
        
        if i == 0:
            return (capacity // wt[0]) * val[0]
        
        if dp[i][capacity]:
            return dp[i][capacity]
            
        not_take = 0 + self.ks(i-1, capacity, val, wt, dp)
        take = float('-inf')
        if wt[i] <= capacity:
            take = val[i] + self.ks(i, capacity-wt[i], val, wt, dp)
        dp[i][capacity] = max(take, not_take)
        return dp[i][capacity]
    
    
    
    def knapSack(self, val, wt,capacity):
        m = len(val)
        dp = [[None for _ in range(capacity + 1)] for _ in range(m)]
        return self.ks(m-1, capacity, val, wt, dp)