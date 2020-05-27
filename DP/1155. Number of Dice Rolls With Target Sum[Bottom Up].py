"""1155. Number of Dice Rolls With Target Sum [Bottom Up]
"""

class Solution:
    
    def numRollsToTarget(self, d, f, t):
        dp = [[0 for _ in range(t+1)]for _ in range(d+1)]
        dp[0][0] = 1
        for d in range(1, d+1):
            for t in range(1, t+1):
                for i in range(1, f+1):
                    if t >= i:
                        dp[d][t] += (dp[d-1][t-i]) % (1000000007)
        return dp[d][t] % (1000000007)