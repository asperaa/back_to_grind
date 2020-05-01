"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""509. Fibonacci Number [Top-Down DP]
"""

class Solution:

    def fib_helper(self, n):
        if n <= 1:
            return n
        if self.dp[n]:
            return self.dp[n]
        self.dp[n] = self.fib_helper(n-1) + self.fib_helper(n-2)
        return self.fib_helper(n)
    
    def fib(self, n):
        self.dp = [None] * (n+1)
        return self.fib_helper(n)  