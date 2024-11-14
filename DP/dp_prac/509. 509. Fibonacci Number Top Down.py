"We are the captains of our ships and we stay till the end. We see our stories through."

class Solution:
    
    def fib_helper(self, n):
        if n < 2:
            return n
        if self.dp[n]:
            return self.dp[n]
        self.dp[n] = self.fib_helper(n-1) + self.fib_helper(n-2)
        return self.dp[n]

    
    
    def fib(self, n: int) -> int:
        self.dp = [None] * (n+1)
        return self.fib_helper(n)
        
    
        