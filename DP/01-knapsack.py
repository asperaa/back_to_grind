# https://www.geeksforgeeks.org/problems/0-1-knapsack-problem0945/1


class Solution:
    
    def ks(self, i, capacity, val, wt):
        if i==0:
            if wt[0] <= capacity:
                return val[0]
            else:
                return 0
        if self.dp[i][capacity]:
            return self.dp[i][capacity]
        not_pick = self.ks(i-1, capacity, val, wt)
        pick = float('-inf')
        if wt[i] <= capacity:
            pick = val[i] + self.ks(i-1, capacity-wt[i], val, wt)
        self.dp[i][capacity] = max(pick, not_pick)
        return self.dp[i][capacity]
    
    
    
    
    
    
    # Function to return max value that can be put in knapsack of capacity.
    def knapSack(self, capacity, val, wt):
        m = len(val)
        self.dp = [[None for _ in range(capacity+1)] for _ in range(m)]
        return self.ks(m-1, capacity, val, wt)
