"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""887. Super Egg Drop
"""

class Solution:

    def superEggDrop(self, e, f):
        dp = [[None for _ in range(f+1)]for _ in range(e+1)]
        return self.super_helper(e, f, dp)
    
    def super_helper(self, e, f, dp):
        if f == 0 or f == 1 or e == 1:
            return f
        if dp[e][f]:
            return dp[e][f]
        min_attempts = float('inf')
        for k in range(f+1):
            attempts = 1 + max(self.super_helper(e-1, f-1, dp), self.super_helper(e, f-k, dp))
            min_attempts = min(min_attempts, attempts)
        return min_attempts