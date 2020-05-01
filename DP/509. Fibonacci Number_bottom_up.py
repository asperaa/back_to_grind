"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""509. Fibonacci Number [Bottom up DP]
"""

class Solution:
    
    def fib(self, n):
        if n == 0:
            return 0
        dp = [None] * (n+1)
        dp[0] = 0
        dp[1] = 1
        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n] 