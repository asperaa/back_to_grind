"We are the captains of ou ships, we stay 'till the end. We see our stories through."

class Solution:
    def climb_stairs_helper(self, n):
        if n <= 2:
            return n
        if self.dp[n]:
            return self.dp[n]
        self.dp[n] = self.climb_stairs_helper(n-1) + self.climb_stairs_helper(n-2)
        return self.dp[n]


    def climbStairs(self, n: int) -> int:
        self.dp = [None] * (n+1)
        return self.climb_stairs_helper(n) 
