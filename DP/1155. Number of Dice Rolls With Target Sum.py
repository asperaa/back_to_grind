"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""1155. Number of Dice Rolls With Target Sum
"""

class Solution:
    
    def numRollsToTarget(self, d, f, t):
        dp = [[None for _ in range(t+1)]for _ in range(d+1)]
        return self.helper(d, f, t, dp)

    
    def helper(self, d, f, t, dp):
        if dp[d][t]:
            return dp[d][t]
        if t == 0 and d == 0:
            return 1
        if d == 0:
            return 0
        summ = 0
        for i in range(1, f+1):
            if t >= i:
                summ += self.helper(d-1, f, t-i, dp)
        dp[d][t] = summ
        return summ
        