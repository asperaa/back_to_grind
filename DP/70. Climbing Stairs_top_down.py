"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""70. Climbing Stairs [Top Down]
"""

class Solution:

    def climbStairsHelper(self, n):
        if n == 1:
            return 1
        if n == 2:
            return 2
        if self.dp[n]:
            return self.dp[n]
        self.dp[n] = self.climbStairsHelper(n-1) + self.climbStairsHelper(n-2)
        return self.climbStairsHelper(n)
    
    def climbStairs(self, n):
        self.dp = [None] * (n+1)
        return self.climbStairsHelper(n)

        