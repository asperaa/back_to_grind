"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""70. Climbing Stairs [Bottom up]
"""

class Solution:

    def climbStairs(self, n):
        if n == 1:
            return 1
        if n == 2:
            return 2
        dp = [None] * (n+1)
        dp[0] = -1
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]